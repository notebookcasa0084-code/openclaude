import sys
from openclaude import DEFAULT_MODEL, ask_llm, search_web


def main():
    print(f"🤖 Iniciando OpenClaude CLI (Modelo: {DEFAULT_MODEL})")
    print("Digite 'sair' ou 'exit' para encerrar a sessão.\n")

    # Lista para armazenar o histórico multi-turno da conversa
    messages = []

    while True:
        try:
            user_input = input("\nVocê: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["sair", "exit", "quit"]:
                print("Até logo! 👋")
                break

            print("\nPesquisando na web...")
            search_results = search_web(user_input)

            # Monta o prompt incluindo o contexto da web (se houver)
            prompt_content = user_input
            if search_results:
                prompt_content = f"Contexto da web:\n{search_results}\n\nPergunta do usuário: {user_input}"

            # Adiciona a mensagem do usuário ao histórico
            messages.append({"role": "user", "content": prompt_content})

            print("Gerando resposta...")
            response = ask_llm(messages)
            print(f"\nOpenClaude:\n{response}")

            # Adiciona a resposta do assistente ao histórico
            messages.append({"role": "assistant", "content": response})

        except KeyboardInterrupt:
            print("\n\nSessão encerrada pelo usuário. Até logo! 👋")
            sys.exit(0)
        except Exception as e:  # noqa: BLE001
            print(f"\n[❌ Erro]: {e}")


if __name__ == "__main__":
    main()
