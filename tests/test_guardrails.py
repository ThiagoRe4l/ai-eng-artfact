import pytest
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage

from src import guardrails
from src.guardrails import BLOCKED_REPLIES, CONTEXT_MESSAGES, _format_conversation, input_guardrail
from src.schemas import InputClassification


class FakeClassifier:
    """Substitui o classificador real: devolve uma categoria fixa ou lança uma exceção."""

    def __init__(self, result=None, error: Exception | None = None):
        self.result = result
        self.error = error
        self.calls = 0

    def invoke(self, _messages):
        self.calls += 1
        if self.error:
            raise self.error
        return self.result


def use_classifier(monkeypatch, classifier: FakeClassifier) -> None:
    monkeypatch.setattr(guardrails, "_classifier", lambda: classifier)


def run_guardrail(text: str = "oi") -> dict | None:
    state = {"messages": [HumanMessage(text)]}
    return input_guardrail.before_agent(state, runtime=None)


def classification(category: str) -> InputClassification:
    return InputClassification(category=category, reason="teste")


def test_in_scope_passes_through(monkeypatch):
    classifier = FakeClassifier(classification("in_scope"))
    use_classifier(monkeypatch, classifier)
    assert run_guardrail("qual violão pra gospel?") is None
    assert classifier.calls == 1


@pytest.mark.parametrize("category", ["out_of_scope", "injection_or_abuse"])
def test_blocked_categories_return_canned_reply_and_jump_to_end(monkeypatch, category):
    use_classifier(monkeypatch, FakeClassifier(classification(category)))
    result = run_guardrail("qualquer coisa")
    assert result["jump_to"] == "end"
    [reply] = result["messages"]
    assert isinstance(reply, AIMessage)
    assert reply.content == BLOCKED_REPLIES[category]


def test_blocked_replies_cover_every_blocking_category():
    blocking = set(InputClassification.model_fields["category"].annotation.__args__) - {"in_scope"}
    assert set(BLOCKED_REPLIES) == blocking


def test_fail_open_when_classifier_raises(monkeypatch):
    use_classifier(monkeypatch, FakeClassifier(error=RuntimeError("503 UNAVAILABLE")))
    assert run_guardrail("oi") is None  # a mensagem passa para o agente


def test_fail_open_when_classifier_returns_nothing(monkeypatch):
    use_classifier(monkeypatch, FakeClassifier(result=None))
    assert run_guardrail("oi") is None


def test_format_conversation_skips_tool_messages_and_empty_ai_messages():
    messages = [
        HumanMessage("quanto custa o F310?"),
        AIMessage(content="", tool_calls=[{"name": "search_products", "args": {}, "id": "1"}]),
        ToolMessage(content='{"results": []}', tool_call_id="1"),
        AIMessage("Ele custa R$ 699,90."),
        HumanMessage("e em 10x?"),
    ]
    text = _format_conversation(messages)
    assert text.splitlines() == [
        "Cliente: quanto custa o F310?",
        "Assistente: Ele custa R$ 699,90.",
        "Cliente: e em 10x?",
    ]
    assert "results" not in text


def test_format_conversation_keeps_only_last_turns():
    messages = []
    for i in range(1, 6):
        messages += [HumanMessage(f"pergunta {i}"), AIMessage(f"resposta {i}")]
    lines = _format_conversation(messages).splitlines()
    assert len(lines) == CONTEXT_MESSAGES == 4
    assert lines == [
        "Cliente: pergunta 4",
        "Assistente: resposta 4",
        "Cliente: pergunta 5",
        "Assistente: resposta 5",
    ]
