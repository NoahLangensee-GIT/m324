# Führt alle Unit-Tests aus
test:
	python -m unittest discover -s tests

# Führt Tests mit Coverage aus, zeigt die Coverage an
coverage:
	coverage run -m unittest discover -s tests
	coverage report
	@del /f .coverage 2>nul || true
