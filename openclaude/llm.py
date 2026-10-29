import os
import ollama
from dotenv import load_dotenv

load_dotenv()

DEFAULT_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5-coder:1.5b")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")


def ask_llm(messages: list, model: str = DEFAULT_MODEL) -> str:
    """Envia o histórico de mensagens para o modelo Ollama e retorna a resposta."""
    try:
        response = ollama.chat(model=model, messages=messages)
        return response["message"]["content"]
    except Exception as e:  # noqa: BLE001
        return f"Erro ao comunicar com o Ollama: {e}"
