"""Avaliação da busca de produtos com o agente real (chama a API do Gemini).

Cada caso roda numa thread nova. Para cada um, registra os argumentos que o modelo
passou para `search_products`, os product_id retornados, a resposta final e duas
checagens automáticas:

- preço: todo valor em R$ citado na resposta precisa existir no retorno da tool
  (price, final_price ou pix_price);
- busca: quando o caso define produtos esperados, eles precisam aparecer no retorno.

Os resultados ficam em evals/search_results.json. Uma nova execução só roda os casos que
ainda não têm resultado; use --only para escolher casos e refazê-los.

Uso (a partir da raiz do projeto):
    .venv\\Scripts\\python -u evals\\run_search_eval.py            # casos pendentes
    .venv\\Scripts\\python -u evals\\run_search_eval.py --only 6 7  # refaz só esses casos
    .venv\\Scripts\\python -u evals\\run_search_eval.py --delay 10  # pausa entre casos (s)
"""

import argparse
import json
import re
import sys
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.stdout.reconfigure(encoding="utf-8")

from src.assistant import create_assistant  # noqa: E402

REPORT_PATH = ROOT / "evals" / "report_search.md"
STATE_PATH = ROOT / "evals" / "search_results.json"  # resultados já obtidos (permite retomar)
MAX_RETRIES = 5
CALL_TIMEOUT = 90.0  # segundos; chamada que não volta nesse prazo é tratada como erro retentável
DEFAULT_DELAY = 6.0  # segundos entre casos, para respeitar o limite por minuto do free tier


@dataclass
class Case:
    number: int
    message: str
    expected: str = ""
    expect_ids: set[int] = field(default_factory=set)  # todos precisam aparecer no retorno
    expect_any_ids: set[int] = field(default_factory=set)  # pelo menos um precisa aparecer


CASES = [
    Case(1, "quero um violão para iniciantes, qual o valor?", "Violões para iniciante, com preços da tool"),
    Case(2, "to começando a tocar agora, qual violão vc indica?", "Recomendação de violão de entrada"),
    Case(3, "violao barato", "Violões de menor preço, sem acento"),
    Case(4, "tem violão com captação até 1500?", "Eletroacústicos com preço final <= R$ 1.500"),
    Case(5, "quanto ta o yamaha f310", "Yamaha F310 (id 87) com preço da tool", expect_ids={87}),
    Case(6, "o Takamine GD20 ainda está em promoção?", "Promoção encerrada + preço atual", expect_ids={95}),
    Case(7, "quais produtos estão em promoção?", "Os 4 ativos: ids 90, 94, 121, 127", expect_ids={90, 94, 121, 127}),
    Case(8, "tem o Giannini GF-3D?", "Sem estoque + alternativas", expect_ids={96}),
    Case(9, "quero o Shelby SN-7C", "Descontinuado + equivalente", expect_ids={113}),
    Case(10, "o ukulele barítono Kala Cedar está disponível?", "Em breve (id 130)", expect_ids={130}),
    Case(11, "ukulele pra minha filha de 8 anos", "Ukuleles de entrada/soprano"),
    Case(12, "guitarra boa pra metal", "Guitarras adequadas a metal"),
    Case(13, "vocês têm saxofone?", "Categoria sem produtos; não inventar"),
    Case(14, "quanto fica o Crafter HT-100 no pix?", "Preço promocional R$ 1.967,18, sem somar o desconto do PIX", expect_ids={90}),
    Case(15, "violão 7 cordas pra choro", "Shelby SN-7C descontinuado + equivalente", expect_any_ids={113}),
    Case(16, "qual o melhor violão que vocês têm? dinheiro não é problema", "Topo de linha (Martin e Taylor)", expect_any_ids={93, 108, 94, 106}),
    Case(17, "quanto custa uma bateria?", "Baterias com preços da tool"),
    Case(18, "teclado de 88 teclas", "Teclados de 88 teclas"),
]


def message_text(message) -> str:
    return message.text  # propriedade (o uso como método está obsoleto no LangChain 1.x)


def parse_brl(value: str) -> float:
    """'1.967,18' -> 1967.18"""
    return float(value.replace(".", "").replace(",", "."))


def cited_prices(answer: str) -> list[float]:
    return [parse_brl(m) for m in re.findall(r"R\$\s*([\d.]*\d(?:,\d{1,2})?)", answer)]


def numbers_in(text: str) -> set[float]:
    """Números escritos pelo cliente (ex.: '1500' em 'até 1500'), que o agente pode repetir sem inventar."""
    return {parse_brl(m) for m in re.findall(r"\d[\d.]*(?:,\d+)?", text)}


def collect_tool_data(messages: list) -> tuple[list[dict], set[int], set[float]]:
    """Devolve as tool calls do modelo, os product_id retornados e os preços válidos."""
    calls, product_ids, allowed = [], set(), set()
    for msg in messages:
        if msg.type == "ai":
            calls.extend(msg.tool_calls)
        elif msg.type == "tool":
            try:
                data = json.loads(msg.content)
            except (TypeError, json.JSONDecodeError):
                continue
            for product in data.get("results", []):
                product_ids.add(product["product_id"])
                for key in ("price", "final_price", "pix_price"):
                    if key in product:
                        allowed.add(round(float(product[key]), 2))
    return calls, product_ids, allowed


def invoke_with_timeout(agent, payload: dict, config: dict):
    """agent.invoke com prazo. Se a chamada não voltar, levanta TimeoutError e abandona a thread."""
    box: dict = {}

    def target() -> None:
        try:
            box["result"] = agent.invoke(payload, config)
        except BaseException as error:  # noqa: BLE001
            box["error"] = error

    worker = threading.Thread(target=target, daemon=True)
    worker.start()
    worker.join(CALL_TIMEOUT)
    if worker.is_alive():
        raise TimeoutError(f"TIMEOUT: sem resposta do modelo em {CALL_TIMEOUT:.0f}s")
    if "error" in box:
        raise box["error"]
    return box["result"]


def retry_delay(error: Exception, attempt: int) -> float | None:
    """Segundos para esperar se o erro for retentável (429, 503 ou timeout); None caso contrário."""
    if isinstance(error, TimeoutError):
        return 5.0
    text = str(error)
    if not any(token in text for token in ("429", "RESOURCE_EXHAUSTED", "503", "UNAVAILABLE")):
        return None
    match = re.search(r"retry in ([\d.]+)s|retryDelay['\"]?:\s*['\"](\d+)s", text)
    if match:
        return float(match.group(1) or match.group(2)) + 2
    return min(15 * 2**attempt, 120)


def run_case(agent, case: Case) -> dict:
    last_error = ""
    for attempt in range(MAX_RETRIES + 1):
        # Thread nova a cada tentativa, para não herdar estado de uma execução interrompida.
        config = {"configurable": {"thread_id": f"search-eval-{case.number}-{attempt}"}, "recursion_limit": 12}
        payload = {"messages": [{"role": "user", "content": case.message}]}
        try:
            result = invoke_with_timeout(agent, payload, config)
        except Exception as error:  # noqa: BLE001
            last_error = str(error)
            delay = retry_delay(error, attempt)
            if delay is None or attempt == MAX_RETRIES:
                break
            print(f"   {last_error[:80]}... aguardando {delay:.0f}s (tentativa {attempt + 1})", flush=True)
            time.sleep(delay)
            continue

        messages = result["messages"]
        calls, product_ids, allowed = collect_tool_data(messages)
        answer = message_text(messages[-1])
        prices = cited_prices(answer)
        allowed |= numbers_in(case.message)  # valores que o próprio cliente citou não contam como invenção
        invalid = [p for p in prices if not any(abs(p - a) < 0.01 for a in allowed)]
        missing = sorted(case.expect_ids - product_ids)
        any_ok = not case.expect_any_ids or bool(case.expect_any_ids & product_ids)
        return {
            "error": None,
            "model_calls": sum(1 for m in messages if m.type == "ai"),
            "tool_args": [c["args"] for c in calls if c["name"] == "search_products"],
            "product_ids": sorted(product_ids),
            "answer": answer,
            "prices": prices,
            "invalid_prices": invalid,
            "price_ok": not invalid,
            "search_ok": not missing and any_ok,
            "missing_ids": missing if missing else (sorted(case.expect_any_ids) if not any_ok else []),
        }
    return {"error": last_error, "model_calls": 0}


def cell(text: str, limit: int = 120) -> str:
    text = " ".join(str(text).split()).replace("|", "\\|")
    return text if len(text) <= limit else text[: limit - 1] + "…"


def write_report(saved: dict[int, dict]) -> None:
    results = [{"case": c, **saved[c.number]} for c in CASES if c.number in saved]
    done = [r for r in results if not r["error"]]
    price_ok = sum(r["price_ok"] for r in done)
    search_ok = sum(r["search_ok"] for r in done)
    all_ok = sum(r["price_ok"] and r["search_ok"] for r in done)
    calls = sum(r["model_calls"] for r in results)
    errors = [r for r in results if r["error"]]

    lines = [
        "# Relatório de avaliação da busca de produtos",
        "",
        f"Gerado em {datetime.now():%d/%m/%Y %H:%M}. Cada caso roda numa thread nova do agente real.",
        "",
        "## Resumo",
        "",
        f"- Casos com resultado: {len(done)}/{len(CASES)}" + (f" ({len(errors)} com erro)" if errors else ""),
        f"- Checagem de preço (todo R$ citado existe no retorno da tool): {price_ok}/{len(done)}",
        f"- Checagem de busca (produtos esperados retornados): {search_ok}/{len(done)}",
        f"- Passaram nas duas checagens: {all_ok}/{len(done)}",
        f"- Chamadas ao modelo (mensagens do assistente): {calls}",
        "",
        "As checagens são automáticas e limitadas: a de preço só olha valores com `R$` e pode",
        "acusar falso positivo em valores derivados (ex.: economia em reais). O comportamento",
        "esperado de cada caso ainda exige leitura da resposta (seção abaixo).",
        "",
        "## Tabela",
        "",
        "| # | Mensagem | Args da busca | IDs retornados | Preço | Busca | Resposta |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in results:
        c = r["case"]
        if r["error"]:
            lines.append(f"| {c.number} | {cell(c.message)} | - | - | ERRO | ERRO | {cell(r['error'])} |")
            continue
        args = "<br>".join(cell(json.dumps(a, ensure_ascii=False), 90) for a in r["tool_args"]) or "(sem tool)"
        ids = ", ".join(map(str, r["product_ids"])) or "-"
        lines.append(
            f"| {c.number} | {cell(c.message)} | {args} | {cell(ids, 60)} | "
            f"{'✅' if r['price_ok'] else '❌'} | {'✅' if r['search_ok'] else '❌'} | {cell(r['answer'], 140)} |"
        )

    lines += ["", "## Detalhe por caso", ""]
    for r in results:
        c = r["case"]
        lines += [f"### {c.number}. {c.message}", ""]
        if c.expected:
            lines.append(f"- **Esperado:** {c.expected}")
        if r["error"]:
            lines += [f"- **Erro:** {r['error']}", ""]
            continue
        lines.append(f"- **Chamadas ao modelo:** {r['model_calls']}")
        for i, args in enumerate(r["tool_args"], 1):
            lines.append(f"- **search_products #{i}:** `{json.dumps(args, ensure_ascii=False)}`")
        if not r["tool_args"]:
            lines.append("- **search_products:** não foi chamada")
        lines.append(f"- **IDs retornados:** {r['product_ids']}")
        if r["invalid_prices"]:
            lines.append(f"- **Preços citados que não vieram da tool:** {r['invalid_prices']}")
        if r["missing_ids"]:
            lines.append(f"- **Produtos esperados que não vieram:** {r['missing_ids']}")
        lines += ["- **Resposta:**", ""]
        lines += [f"  > {line}" if line else "  >" for line in r["answer"].splitlines()]
        lines.append("")

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--only", type=int, nargs="+", help="números dos casos a (re)executar")
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY, help="pausa entre casos, em segundos")
    args = parser.parse_args()

    saved: dict[int, dict] = {}
    if STATE_PATH.exists():
        saved = {int(k): v for k, v in json.loads(STATE_PATH.read_text(encoding="utf-8")).items()}

    pending = lambda c: c.number not in saved or saved[c.number]["error"]  # noqa: E731
    cases = [c for c in CASES if (c.number in args.only if args.only else pending(c))]
    if not cases:
        print("Nada a executar: todos os casos já têm resultado (use --only para refazer).")
        return

    agent = create_assistant()
    for index, case in enumerate(cases):
        print(f"[{index + 1}/{len(cases)}] {case.message}", flush=True)
        result = run_case(agent, case)
        saved[case.number] = result
        if result["error"]:
            print(f"   ERRO: {result['error'][:200]}", flush=True)
        else:
            print(
                f"   tool={result['tool_args']} ids={result['product_ids']} "
                f"preço={'ok' if result['price_ok'] else 'FALHOU'} busca={'ok' if result['search_ok'] else 'FALHOU'}",
                flush=True,
            )
        # Casos com erro também ficam salvos (aparecem no relatório) e são refeitos na próxima execução.
        STATE_PATH.write_text(json.dumps(saved, ensure_ascii=False, indent=1), encoding="utf-8")
        write_report(saved)  # grava a cada caso, para não perder o progresso
        if index < len(cases) - 1:
            time.sleep(args.delay)
    print(f"\nRelatório salvo em {REPORT_PATH}")


if __name__ == "__main__":
    main()
