import sys
from src.assistant import create_assistant
from src.config import validate_environment

def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

def main() -> None:
    try:
        validate_environment()
    except RuntimeError as e:
        print(f"Erro de configuração: {e}")
        return

    agent = create_assistant()
    config = {"configurable": {"thread_id": "cli-1"}, "recursion_limit": 12}
    print("Vendedor/Assistente da Empório da Música - (digite 'sair' para encerrar)\n")

    try:
        while True:
            question = input("> ").strip()
            if not question:
                continue
            if question.lower() == "sair":
                break
            try:
                response = agent.invoke(
                    {"messages": [{"role": "user", "content": question}]},
                    config,
                )
                print(response["messages"][-1].text, "\n")
            except Exception as e:
                print(f"Erro ao processar a pergunta: {e}\n")
    except (KeyboardInterrupt, EOFError):
        print()

    print("Encerrando o assistente...")

if __name__ == "__main__":
    main()