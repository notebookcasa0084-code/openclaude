from duckduckgo_search import DDGS

def search_web(query: str, max_results: int = 3) -> str:
    """Realiza uma busca na web via DuckDuckGo e retorna os resultados concatenados."""
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
