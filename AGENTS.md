# AGENTS.md

## Project summary

This repository publishes a generated Python client for the DefectDojo v2 API.

- Runtime package: `defectdojo_api_generated`
- Primary public entry point: `defectdojo_api_generated.client.DefectDojo`
- Generator source: OpenAPI Generator with custom mustache templates under `support/api_generation/custom_templates`
- Upstream schema source: DefectDojo OpenAPI schema fetched and lightly patched under `support/openapi`

The codebase is mostly generated. The important mental model is:

1. Fetch or refresh the OpenAPI schema.
2. Apply small schema tweaks that add generator hints.
3. Regenerate the package and generated tests.
4. Keep handwritten customization in templates or helper modules, not in generated API/model files.

## Repo layout

### Generated runtime package

- `defectdojo_api_generated/api/`
  One generated class per API area. These files are large and should be treated as generated output.
- `defectdojo_api_generated/models/`
  Generated Pydantic request/response models.
- `defectdojo_api_generated/__init__.py`
  Generated package export surface and version metadata.
- `defectdojo_api_generated/api_client.py`
  Generated HTTP client core.
- `defectdojo_api_generated/configuration.py`, `rest.py`, `exceptions.py`, `api_response.py`
  Generated runtime plumbing.

### Handwritten or customized runtime pieces

- `defectdojo_api_generated/client.py`
  Custom convenience wrapper exposing lazily constructed `*_api` properties and simpler auth setup.
- `defectdojo_api_generated/helpers.py`
  Handwritten pagination helper used by generated iterator methods.

### Generation pipeline

- `support/openapi/fetch_openapi.py`
  Fetches the DefectDojo schema from either the live demo or a local Docker-backed instance.
- `support/openapi/tweak_openapi.py`
  Adds custom vendor extensions for paginated endpoints so generated API classes expose iterator helpers.
- `support/openapi/openapi.json`
  Stored raw schema snapshot.
- `support/openapi/build/openapi.json`
  Tweaked schema used for generation.
- `support/api_generation/generate.sh`
  Runs schema tweaking, OpenAPI Generator, and moves generated tests into `tests/generated/`.
- `support/api_generation/config.yaml`
  OpenAPI Generator config.
- `support/api_generation/custom_templates/`
  The real customization layer. If generation behavior needs to change, edit templates here rather than the generated output.
- `support/api_generation/templates.spec/`
  Reference snapshot of template files.

### Tests

- `tests/generated/`
  Generated smoke tests for API and model classes. Expect these to be overwritten on regeneration.
- `tests/unit/`
  Small handwritten unit tests for custom client behavior.
- `tests/integration/`
  End-to-end tests against a real DefectDojo instance.
- `tests/data/`
  Fixtures for integration scenarios, such as import/reimport payloads.

ALWAYS use unittest.TestCase to write new tests unless you really cannot.

### Local integration environment

- `support/integration/docker-compose.yml`
  Local DefectDojo stack for schema refreshes and integration testing.
- `support/integration/run_dojo.sh`
  Starts the stack and waits for the API to become ready.
- `support/integration/stop_dojo.sh`
  Stops the stack.

## How the client works

The package is intentionally thin:

- `DefectDojo(...)` builds a `Configuration`, infers proxy settings from the environment, and creates one shared `ApiClient`.
- Each `*.api` property on `DefectDojo` returns a generated API wrapper bound to that shared client.
- Generated API methods serialize parameters, call the generated `ApiClient`, then deserialize into Pydantic models.
- For paginated GET endpoints, `support/openapi/tweak_openapi.py` annotates the schema with `x-has-iterator`, and the custom `api.mustache` template emits `*_iterator()` helpers that stream results across pages via `helpers.get_all_pages()`.

## Safe editing rules

Prefer these rules unless a task explicitly requires regeneration:

- Do not hand-edit files in `defectdojo_api_generated/api/`.
- Do not hand-edit files in `defectdojo_api_generated/models/`.
- Treat `tests/generated/` as generated output.
- If a change should survive regeneration, make it in:
  - `support/api_generation/custom_templates/`
  - `support/openapi/tweak_openapi.py`
  - `support/openapi/fetch_openapi.py`
  - `defectdojo_api_generated/helpers.py`
  - `defectdojo_api_generated/client.py`
  - handwritten tests in `tests/unit/` or `tests/integration/`

When deciding where to edit:

- API signature/serialization/runtime generation issue: fix a mustache template or schema tweak.
- Pagination iteration issue: check `tweak_openapi.py`, `custom_templates/api.mustache`, and `helpers.py`.
- Convenience client/auth/proxy behavior: check `client.py`.
- Upstream API shape drift: refresh schema, regenerate, then review diffs.

## Common commands

Environment:

- `uv sync --dev`

Formatting and lint:

- `make lint`
- `make lint-check`

Repo-specific expectation:

- After any code, template, packaging, or GitHub Actions change, run `make lint`.
- Do not treat `make lint` as optional or defer it unless the user explicitly asks not to run it or you are blocked.

Tests:

- `make test`
- `make test-e2e`

Schema and generation:

- `make schema`
- `make generate`
- `make templates`

Publishing helper:

- `make testpub`

## Regeneration workflow

Use this when the DefectDojo API changed or when template/schema customizations need to be applied across the client:

1. Refresh dependencies with `uv sync --dev`.
2. Fetch schema with `make schema` or run `support/openapi/fetch_openapi.py --demo`.
3. Regenerate with `make generate`.
4. Review diffs carefully in:
   - `defectdojo_api_generated/`
   - `tests/generated/`
5. Run `make test`.
6. If integration behavior changed, run `make test-e2e`.

## CI and release notes

- CI runs lint, unit tests on multiple Python versions, and integration tests via GitHub Actions.
- Packaging metadata lives in `pyproject.toml`.
- Release publishing is tag-driven via `.github/workflows/publish-main.yml`.
- The package targets Python `>=3.9,<4`.

## Practical contributor notes

- The repository currently includes generated artifacts and some local cache directories; focus changes on tracked source files.
- `README.md` is minimal and points contributors to `CONTRIBUTING.md`; this file is the better quick orientation for agentic work.
- If generated output and handwritten files disagree, assume templates and schema-tweaking scripts are the source of truth, then regenerate instead of patching the generated leaf files by hand.
