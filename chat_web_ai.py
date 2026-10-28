import sys
import ollama
from duckduckgo_search import DDGS

def search_web(query, max_results=3):
    print(f"\n[🔍 Pesquisa Web] Buscando informações recentes sobre: '{query}'...")
    results = []
    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                results.append(r['body'])
        return "\n".join(results)
    except Exception as e:
        print(f"[⚠️ Alerta] Falha ao realizar busca web: {e}")
        return ""

def main():
    print("=" * 60)
    print("🤖 Chat OpenClaude (Qwen2.5-Coder + Busca Web)")
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

            # Executa a busca web com o input do usuário
            web_context = search_web(user_input)

            if web_context:
                prompt_with_context = f"""Responda à pergunta do usuário utilizando as informações contextuais obtidas da web abaixo.

Contexto da Web:
{web_context}

Pergunta do Usuário: {user_input}
"""
            else:
                prompt_with_context = user_input

            print("\n🤖 Qwen: ", end="", flush=True)

            # Faz a chamada para o Ollama com streaming para respostas em tempo real
            stream = ollama.chat(
                model='qwen2.5-coder:1.5b',
                messages=[{'role': 'user', 'content': prompt_with_context}],
                stream=True
            )

            for chunk in stream:
                print(chunk['message']['content'], end='', flush=True)
            print()

        except KeyboardInterrupt:
            print("\n\nSessão encerrada pelo usuário. Até logo! 👋")
            sys.exit(0)
        except Exception as e:
            print(f"\n[❌ Erro]: {e}")

if __name__ == "__main__":
    main()
