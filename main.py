import sys
from src.assistant import create_assistant
from src.config import validate_environment
from rich.console import Console
from rich.markdown import Markdown
from src.prompts import GREETING

console = Console()

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
    print("Assistente da Empório da Música - (digite 'sair' para encerrar)\n")

    greeted = False

    try:
        while True:
            question = input("> ").strip()
            if not question:
                continue
            if question.lower() == "sair":
                break
            if not greeted:
                console.print(Markdown(GREETING))
                print()
                greeted = True
            try:
                response = agent.invoke(
                    {"messages": [{"role": "user", "content": question}]},
                    config,
                )
                console.print(Markdown(response["messages"][-1].text))
                print()
            except Exception as e:
                print(f"Erro ao processar a pergunta: {e}\n")
    except (KeyboardInterrupt, EOFError):
        print()

    print("Encerrando o assistente...")

if __name__ == "__main__":
    main()