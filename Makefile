lint:
	uv run ruff format
	uv run ruff check --fix

lint-check:
	uv run ruff format --diff
	uv run ruff check

test:
	if [ -n "$(GITHUB_RUN_ID)" ]; then \
		uv run python -m pytest --cov --cov-report=xml --junitxml=junit.xml -o junit_family=legacy; \
	else \
		uv run python -m pytest --cov; \
	fi

test-e2e: export DD_INTEGRATION_TESTS=1
test-e2e:
	python -m pytest tests/integration

testpub:
	rm -fr dist
	uv run pyproject-build
	uv run twine upload --repository testpypi dist/*

schema:
	./support/openapi/fetch_openapi.py

templates:
	./support/api_generation/dump_templates.sh

generate:
	./support/api_generation/generate.sh
	$(MAKE) lint
