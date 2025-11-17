test: src/file.py tests/test.py
	python -m unittest discover -s tests
	rm -rf src/__pycache__
	rm -rf tests/__pycache__

coverage:
	coverage run -m unittest discover -s tests
	coverage report
	rm -f .coverage
