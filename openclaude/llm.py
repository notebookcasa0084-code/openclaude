import os
from typing import cast

import ollama
from dotenv import load_dotenv

from openclaude.logger import get_logger

load_dotenv()
logger = get_logger("openclaude.llm")

DEFAULT_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5-coder:1.5b")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")


def ask_llm(messages: list, model: str = DEFAULT_MODEL) -> str:
    """Envia o histórico de mensagens para o modelo Ollama e retorna a resposta."""
    try:
        logger.info(f"Enviando requisição para o modelo Ollama ({model})...")
        response = ollama.chat(model=model, messages=messages)
        content = response["message"]["content"]
        return cast(str, content)
    except Exception as e:  # noqa: BLE001
        logger.error(f"Erro ao comunicar com o Ollama: {e}")
        return f"Erro ao comunicar com o Ollama: {e}"
