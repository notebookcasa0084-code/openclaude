import os

import ollama
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

DEFAULT_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5-coder:1.5b")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")


def ask_llm(prompt: str, model: str = DEFAULT_MODEL) -> str:
    """Envia um prompt para o modelo Ollama configurado e retorna a resposta."""
    try:
        response = ollama.chat(
            model=model, messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]
    except Exception as e:  # noqa: BLE001
        return f"Erro ao comunicar com o Ollama: {e}"
