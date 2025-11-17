.PHONY: integration-test

integration-test: src/user.py src/db.py tests/testdb.py
	python3 -m unittest tests/testdb.py
	rm -rf src/__pycache__
	rm -rf tests/__pycache__
