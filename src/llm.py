from langchain.chat_models import init_chat_model

from src.config import MODEL_ID, validate_environment

def get_model():
    return init_chat_model(MODEL_ID)

def test_model() -> str:
    validate_environment()
    model = get_model()
    response = model.invoke("Diga apenas: 'Conexão com o modelo OK'.")
    return response.text