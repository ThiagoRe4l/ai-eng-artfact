from types import SimpleNamespace

import pytest

import main


class FakeAgent:
    def __init__(self):
        self.calls = []

    def invoke(self, payload, config=None):
        self.calls.append(payload)
        return {"messages": [SimpleNamespace(text="resposta falsa")]}


def run_main(monkeypatch, inputs):
    """Roda main.main() com agente falso e input simulado.

    Cada item de `inputs` é devolvido pelo input(); se for uma exceção, ela é lançada.
    """
    agent = FakeAgent()
    items = iter(inputs)

    def fake_input(prompt=""):
        item = next(items)
        if isinstance(item, BaseException):
            raise item
        return item

    monkeypatch.setattr(main, "validate_environment", lambda: None)
    monkeypatch.setattr(main, "create_assistant", lambda: agent)
    monkeypatch.setattr("builtins.input", fake_input)
    main.main()
    return agent


def test_empty_input_is_ignored(monkeypatch, capsys):
    agent = run_main(monkeypatch, ["", "   ", "sair"])
    assert agent.calls == []
    assert "Encerrando o assistente..." in capsys.readouterr().out


def test_sair_exits_without_calling_agent(monkeypatch, capsys):
    agent = run_main(monkeypatch, ["sair"])
    assert agent.calls == []
    assert "Encerrando o assistente..." in capsys.readouterr().out


def test_sair_is_case_insensitive(monkeypatch, capsys):
    run_main(monkeypatch, ["  SAIR "])
    assert "Encerrando o assistente..." in capsys.readouterr().out


def test_question_reaches_agent_and_answer_is_printed(monkeypatch, capsys):
    agent = run_main(monkeypatch, ["ola", "sair"])
    out = capsys.readouterr().out
    assert agent.calls == [{"messages": [{"role": "user", "content": "ola"}]}]
    assert "resposta falsa" in out


@pytest.mark.parametrize("exc", [KeyboardInterrupt(), EOFError()])
def test_interrupt_and_eof_exit_cleanly(monkeypatch, capsys, exc):
    run_main(monkeypatch, [exc])  # não deve levantar exceção
    out = capsys.readouterr().out
    assert "Encerrando o assistente..." in out
    assert "Traceback" not in out


def test_agent_error_does_not_crash_loop(monkeypatch, capsys):
    class BrokenAgent(FakeAgent):
        def invoke(self, payload, config=None):
            raise RuntimeError("503 UNAVAILABLE")

    monkeypatch.setattr(main, "validate_environment", lambda: None)
    monkeypatch.setattr(main, "create_assistant", lambda: BrokenAgent())
    items = iter(["ola", "sair"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(items))
    main.main()
    out = capsys.readouterr().out
    assert "Erro ao processar a pergunta: 503 UNAVAILABLE" in out
    assert "Encerrando o assistente..." in out
