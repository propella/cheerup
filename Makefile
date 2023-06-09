install:
	pip install -e .[dev]

format:
	black .

mypy:
	mypy --disallow-untyped-defs src/cheer

.PHONY: install
