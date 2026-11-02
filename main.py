from src.config import MODEL_ID, validate_environment

def main() -> None:
    validate_environment()
    print(f"Vendedor/Assistente da Empório da Música - projeto inicializado!")
    print(f"Using model: {MODEL_ID}")

if __name__ == "__main__":
    main()