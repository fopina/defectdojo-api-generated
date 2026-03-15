## Build

This project uses `uv`, so set up the virtualenv by running

```
uv sync --dev
```

Use `make test` to make sure all tests pass before pushing.

Use `make lint` to make sure lint check passes before pushing.

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

...
