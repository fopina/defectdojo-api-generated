lint:
	ruff format
	ruff check --fix
	pyproject-pipenv --fix

lint-check:
	ruff format --diff
	ruff check
	pyproject-pipenv

test:
	if [ -n "$(GITHUB_RUN_ID)" ]; then \
		pytest --cov --cov-report=xml --junitxml=junit.xml -o junit_family=legacy; \
	else \
		python -m pytest --cov; \
	fi

testpub:
	rm -fr dist
	pyproject-build
	twine upload --repository testpypi dist/*
