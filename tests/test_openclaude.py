from openclaude import DEFAULT_MODEL, __version__


def test_package_metadata():
    """Garante que a versão do pacote e o modelo padrão estão definidos corretamente."""
    assert __version__ == "1.0.0"
    assert DEFAULT_MODEL == "qwen2.5-coder:1.5b"

def test_import_modules():
    """Garante que os submódulos principais podem ser importados sem erros."""
    from openclaude import ask_llm, search_web
    assert callable(search_web)
    assert callable(ask_llm)
