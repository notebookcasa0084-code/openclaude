import ollama
from typing import Generator

DEFAULT_MODEL = "qwen2.5-coder:1.5b"

def generate_stream(prompt: str, context: str = "", model: str = DEFAULT_MODEL) -> Generator[str, None, None]:
    """Envia o prompt e o contexto para o Ollama e gera tokens via streaming."""
    if context:
        full_prompt = f"""Responda à pergunta do usuário utilizando as informações contextuais obtidas da web abaixo.

Contexto da Web:
{context}

Pergunta do Usuário: {prompt}
"""
    else:
        full_prompt = prompt

    stream = ollama.chat(
        model=model,
        messages=[{'role': 'user', 'content': full_prompt}],
        stream=True
    )

    for chunk in stream:
        yield chunk['message']['content']
