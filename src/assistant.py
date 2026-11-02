from langchain.agents import create_agent
from langchain.agents.middleware import ModelRequest, dynamic_prompt
from langgraph.checkpoint.memory import InMemorySaver

from src.config import AGENT_MODEL_ID
from src.prompts import build_system_prompt
from src.tools import get_order_status, search_policies, search_products

@dynamic_prompt
def current_system_prompt(request: ModelRequest) -> str:
    """Recria o prompt do sistema a cada chamada de modelo, garantindo que a data e a hora nunca fiquem desatualizadas.."""
    return build_system_prompt()

def create_assistant():
    return create_agent(
        model=AGENT_MODEL_ID,
        tools=[search_products, search_policies,get_order_status],
        middleware=[current_system_prompt],
        checkpointer=InMemorySaver(),
    )