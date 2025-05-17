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
		python -m pytest --cov --cov-report=xml --junitxml=junit.xml -o junit_family=legacy; \
	else \
		python -m pytest --cov; \
	fi

test-e2e: export DD_INTEGRATION_TESTS=1
test-e2e:
	python -m pytest tests/integration

testpub:
	rm -fr dist
	pyproject-build
	twine upload --repository testpypi dist/*

schema:
	./support/fetch_openapi.py

templates:
	./support/api_generation/dump_templates.sh

generate:
	./support/api_generation/generate.sh
	$(MAKE) lint
