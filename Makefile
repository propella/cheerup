install:
	pip install -e .[dev]

format:
	black .

mypy:
	mypy --disallow-untyped-defs src/cheerup

.PHONY: install
