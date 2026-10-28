import sys
from openclaude import search_web, generate_stream, DEFAULT_MODEL

def main():
    print("=" * 60)
    print("🤖 OpenClaude CLI (Arquitetura Modular)")
    print(f"Modelo Ativo: {DEFAULT_MODEL}")
    print("Digite sua pergunta abaixo. Digite 'sair' ou 'exit' para encerrar.")
    print("=" * 60 + "\n")

    while True:
        try:
            user_input = input("\n👤 Você: ").strip()
            
            if not user_input:
                continue

            if user_input.lower() in ["sair", "exit", "quit"]:
                print("\nEncerrando sessão. Até logo! 👋")
                sys.exit(0)

            # 1. Módulo de Busca Web
            web_context = search_web(user_input)

            print("\n🤖 OpenClaude: ", end="", flush=True)

            # 2. Módulo de LLM (Streaming)
            for token in generate_stream(prompt=user_input, context=web_context):
                print(token, end="", flush=True)
            print()

        except KeyboardInterrupt:
            print("\n\nSessão encerrada pelo usuário. Até logo! 👋")
            sys.exit(0)
        except Exception as e:
            print(f"\n[❌ Erro]: {e}")

if __name__ == "__main__":
    main()
