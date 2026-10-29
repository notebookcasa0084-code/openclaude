import sys

from openclaude import DEFAULT_MODEL, ask_llm, search_web


def main():
    print(f"🤖 Iniciando OpenClaude CLI (Modelo: {DEFAULT_MODEL})")
    print("Digite 'sair' ou 'exit' para encerrar a sessão.\n")

    while True:
        try:
            user_input = input("\nVocê: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["sair", "exit", "quit"]:
                print("Até logo! 👋")
                break

            # Exemplo básico de uso integrado (busca web + LLM)
            print("\nPesquisando na web...")
            search_results = search_web(user_input)
            
            prompt = f"Contexto da web:\n{search_results}\n\nPergunta do usuário: {user_input}"
            
            print("Gerando resposta...")
            response = ask_llm(prompt)
            print(f"\nOpenClaude:\n{response}")

        except KeyboardInterrupt:
            print("\n\nSessão encerrada pelo usuário. Até logo! 👋")
            sys.exit(0)
        except Exception as e:  # noqa: BLE001
            print(f"\n[❌ Erro]: {e}")

if __name__ == "__main__":
    main()
