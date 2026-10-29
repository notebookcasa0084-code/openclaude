install:
	pip install -r requirements.txt

run:
	python main.py

test:
	pytest --cov=openclaude --cov-report=term-missing

lint:
	ruff check .

typecheck:
	mypy openclaude/ main.py

format:
	ruff format .
