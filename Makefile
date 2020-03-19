install:
	python3 -m venv .venv
	.venv/bin/pip install sphinx

makedoc:
	.venv/bin/sphinx-build doc/source doc/build
