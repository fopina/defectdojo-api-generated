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

testpub:
	rm -fr dist
	pyproject-build
	twine upload --repository testpypi dist/*

schema:
	curl "https://demo.defectdojo.org/api/v2/oa3/schema/?format=json" -o support/openapi.json

generate:
	./support/api_generation/dump_templates.sh
	./support/api_generation/generate.sh
	$(MAKE) lint
