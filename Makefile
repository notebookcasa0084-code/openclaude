.PHONY: help run test clean install

help:
	@echo "Comandos disponíveis no OpenClaude:"
	@echo "  make install - Instala as dependências do requirements.txt"
	@echo "  make run     - Executa a interface CLI do chat modular"
	@echo "  make test    - Roda a suíte de testes unitários com pytest"
	@echo "  make clean   - Remove arquivos temporários de cache do Python e pytest"

install:
	pip install -r requirements.txt --break-system-packages

run:
	python3 main.py

test:
	pytest

clean:
	rm -rf .pytest_cache __pycache__ openclaude/__pycache__ tests/__pycache__
