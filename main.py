import sys

from openclaude import DEFAULT_MODEL, ask_llm, get_logger, search_web

logger = get_logger("openclaude.main")


def main():
    logger.info(f"Iniciando OpenClaude CLI (Modelo: {DEFAULT_MODEL})")
    print(f"🤖 Iniciando OpenClaude CLI (Modelo: {DEFAULT_MODEL})")
    print("Digite 'sair' ou 'exit' para encerrar a sessão.\n")

    messages = []

    while True:
        try:
            user_input = input("\nVocê: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["sair", "exit", "quit"]:
                logger.info("Sessão encerrada pelo usuário.")
                print("Até logo! 👋")
                break

            search_results = search_web(user_input)

            prompt_content = user_input
            if search_results:
                prompt_content = f"Contexto da web:\n{search_results}\n\nPergunta do usuário: {user_input}"

            messages.append({"role": "user", "content": prompt_content})

            response = ask_llm(messages)
            print(f"\nOpenClaude:\n{response}")

            messages.append({"role": "assistant", "content": response})

        except KeyboardInterrupt:
            logger.info("Sessão encerrada por KeyboardInterrupt.")
            print("\n\nSessão encerrada pelo usuário. Até logo! 👋")
            sys.exit(0)
        except Exception as e:
            logger.exception(f"Erro inesperado na CLI: {e}")
            print(f"\n[❌ Erro]: {e}")


if __name__ == "__main__":
    main()
