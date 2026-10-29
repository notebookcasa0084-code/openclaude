from .llm import DEFAULT_MODEL, ask_llm
from .logger import get_logger
from .search import search_web

__version__ = "1.0.0"
__all__ = ["DEFAULT_MODEL", "ask_llm", "get_logger", "search_web"]
