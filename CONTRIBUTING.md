## Build

This project uses `uv`, so set up the virtualenv by running

```
uv sync --dev
```

Use `make test` to make sure all tests pass before pushing.

Use `make lint` to make sure lint check passes before pushing.

## Packaging layout

The main package, `defectdojo-api-generated`, is intentionally library-only.
It does not publish console scripts and should remain installable without CLI-only dependencies.

The `dojo` entrypoint lives in the thin wrapper package under `packages/cli/`.
That package depends on the main library plus the CLI stack and should stay small:
keep CLI packaging, entrypoints, and CLI-only dependency wiring there, while the actual CLI implementation can continue to live under `defectdojo_api_generated/cli/`.

## Guidelines

### Update openapi-generator version

* Run `make templates`
* Generate diff from `support/api_generation/custom_templates` with `support/api_generation/templates.spec`
  * Create new temporary branch
  * `make templates` / `rm -fr support/api_generation/custom_templates/*` / `mv support/api_generation/templates.spec/* support/api_generation/custom_templates/`
  * Push and create PR (to be closed without merge) - use it as reference for changes
  * Back to upgrade branch
* Update version in `support/api_generation/openapi-generator-cli.sh`
* Run `make templates` again
* Update `support/api_generation/custom_templates` with the new templates considering the changes from first step
  * `rm -fr support/api_generation/custom_templates/*` / `mv support/api_generation/templates.spec/* support/api_generation/custom_templates/`
  * Re-apply changes using the temporary PR created before

### Update Dojo OpenAPI schema

* Run `support/openapi/fetch_openapi.py` to refresh local copy
* `make generate`
