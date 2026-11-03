import logging
from functools import lru_cache

from langchain.agents.middleware import AgentState, before_agent
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langgraph.runtime import Runtime

from src.llm import get_model
from src.prompts import CLASSIFIER_PROMPT
from src.schemas import InputClassification

logger = logging.getLogger(__name__)

CONTEXT_MESSAGES = 4  # As perguntas de acompanhamento curtas ("e em 10x?") precisam da resposta anterior para serem classificadas.

BLOCKED_REPLIES = {
    "out_of_scope": (
        "Opa, nesse assunto eu não consigo ajudar! Por aqui eu cuido de tudo da Empório da Música: "
        "instrumentos, pedidos, pagamento, entrega e trocas. Posso te ajudar com alguma dessas coisas?"
    ),
    "injection_or_abuse": (
        "Isso eu não consigo fazer, mas fico feliz em ajudar com instrumentos, pedidos "
        "ou dúvidas sobre a loja. O que você está procurando?"
    ),
}


@lru_cache(maxsize=1)
def _classifier():
    return get_model().with_structured_output(InputClassification)


def _format_conversation(messages: list[BaseMessage]) -> str:
    turns = [
        f"{'Cliente' if m.type == 'human' else 'Assistente'}: {m.text}"
        for m in messages
        if m.type == "human" or (m.type == "ai" and m.text)
    ]
    return "\n".join(turns[-CONTEXT_MESSAGES:])


def classify_input(messages: list[BaseMessage]) -> InputClassification | None:
    """Retorna None quando o classificador falha (fail-open: o agente ainda tem suas próprias regras de escopo)."""
    try:
        return _classifier().invoke(
            [SystemMessage(CLASSIFIER_PROMPT), HumanMessage(_format_conversation(messages))]
        )
    except Exception:
        logger.warning("Input classifier failed; letting the message through.", exc_info=True)
        return None


@before_agent(can_jump_to=["end"])
def input_guardrail(state: AgentState, runtime: Runtime) -> dict | None:
    result = classify_input(state["messages"])
    if result is None or result.category == "in_scope":
        return None
    logger.info("Blocked message (%s): %s", result.category, result.reason)
    return {"messages": [AIMessage(content=BLOCKED_REPLIES[result.category])], "jump_to": "end"}