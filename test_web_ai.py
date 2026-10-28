import ollama
from duckduckgo_search import DDGS

def search_web(query, max_results=3):
    print(f"[Pesquisa Web] Buscando por: '{query}'...")
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append(r['body'])
    return "\n".join(results)

def ask_qwen_with_search(prompt):
    # 1. Busca na internet
    web_context = search_web(prompt)
    
    # 2. Monta o prompt enriquecido com os dados da web
    full_prompt = f"""Responda à pergunta com base no contexto da web abaixo.

Contexto da Web:
{web_context}

Pergunta: {prompt}
"""
    
    print("[Ollama] Gerando resposta com qwen2.5-coder:1.5b...")
    response = ollama.chat(model='qwen2.5-coder:1.5b', messages=[
        {
            'role': 'user',
            'content': full_prompt,
        },
    ])
    
    print("\n--- Resposta da IA ---")
    print(response['message']['content'])

if __name__ == "__main__":
    # Exemplo de teste
    pergunta = "Quais são as principais atualizações de tecnologia em 2026?"
    ask_qwen_with_search(pergunta)
