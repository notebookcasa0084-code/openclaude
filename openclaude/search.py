from duckduckgo_search import DDGS

from openclaude.logger import get_logger

logger = get_logger("openclaude.search")


def search_web(query: str, max_results: int = 3) -> str:
    """Realiza uma busca na web usando o DuckDuckGo e retorna os resultados formatados."""
    try:
        logger.info(f"Realizando busca web para o termo: '{query}'")
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                results.append(r["body"])
        return "\n".join(results)
    except Exception as e:  # noqa: BLE001
        logger.warning(f"Falha ao realizar busca web: {e}")
        return ""
