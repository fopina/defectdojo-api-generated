lint:
	uv run ruff format
	uv run ruff check --fix

lint-check:
	uv run ruff format --diff
	uv run ruff check

.venv39: export VIRTUAL_ENV=.venv39
.venv39:
	uv sync --dev --extra cli --python 3.9 --active

test39: .venv39
test39: export VIRTUAL_ENV=.venv39
test39:
	uv run --active pytest --cov

test39-e2e: .venv39
test39-e2e: export VIRTUAL_ENV=.venv39
test39-e2e: export DD_INTEGRATION_TESTS=1
test39-e2e:
	uv run --active pytest tests/integration/test_e2e.py

test:
	if [ -n "$(GITHUB_RUN_ID)" ]; then \
		uv run pytest --cov --cov-report=xml --junitxml=junit.xml -o junit_family=legacy; \
	else \
		uv run pytest --cov; \
	fi

test-e2e: export DD_INTEGRATION_TESTS=1
test-e2e:
	uv run pytest tests/integration

testpub:
	rm -fr dist
	uv run pyproject-build
	uv run twine upload --repository testpypi dist/*

schema:
	uv run ./support/openapi/fetch_openapi.py --output ./support/openapi/openapi-new.json
	uv run ./support/openapi/openapi_changelog.py ./support/openapi/openapi.json ./support/openapi/openapi-new.json
	mv ./support/openapi/openapi-new.json ./support/openapi/openapi.json

templates:
	./support/api_generation/dump_templates.sh

generate:
	./support/api_generation/generate.sh
	$(MAKE) lint
