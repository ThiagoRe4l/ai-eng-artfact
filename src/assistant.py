from langchain.agents import create_agent
from langchain.agents.middleware import ModelRequest, dynamic_prompt
from langgraph.checkpoint.memory import InMemorySaver

from src.config import AGENT_MODEL_ID
from src.prompts import build_system_prompt

@dynamic_prompt
def current_system_prompt(request: ModelRequest) -> str:
    """Recria o prompt do sistema a cada chamada de modelo, garantindo que a data e a hora nunca fiquem desatualizadas.."""
    return build_system_prompt()

def create_assistant():
    return create_agent(
        model=AGENT_MODEL_ID,
        tools=[],
        middleware=[current_system_prompt],
        checkpointer=InMemorySaver(),
    )