from openclaude import DEFAULT_MODEL, __version__
from openclaude.llm import ask_llm
from openclaude.search import search_web


def test_package_metadata():
    """Garante que a versão do pacote e o modelo padrão estão definidos corretamente."""
    assert __version__ == "1.0.0"
    assert DEFAULT_MODEL == "qwen2.5-coder:1.5b"


def test_import_modules():
    """Garante que os submódulos principais podem ser importados sem erros."""
    from openclaude import ask_llm, search_web

    assert callable(search_web)
    assert callable(ask_llm)


def test_ask_llm_success(mocker):
    """Testa a função ask_llm simulando uma resposta bem-sucedida do Ollama."""
    mock_chat = mocker.patch("ollama.chat")
    mock_chat.return_value = {"message": {"content": "Olá do mock!"}}

    resposta = ask_llm("Teste prompt")
    assert resposta == "Olá do mock!"
    mock_chat.assert_called_once()


def test_search_web_success(mocker):
    """Testa a função search_web simulando resultados do DuckDuckGo."""
    mock_ddgs = mocker.patch("openclaude.search.DDGS")
    mock_instance = mock_ddgs.return_value.__enter__.return_value
    mock_instance.text.return_value = [{"body": "Resultado de teste da web"}]

    resultado = search_web("python test")
    assert "Resultado de teste da web" in resultado
    mock_instance.text.assert_called_once()
