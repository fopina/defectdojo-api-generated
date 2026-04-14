# defectdojo-api-generated

[![ci](https://github.com/fopina/defectdojo-api-generated/actions/workflows/publish-main.yml/badge.svg)](https://github.com/fopina/defectdojo-api-generated/actions/workflows/publish-main.yml)
[![test](https://github.com/fopina/defectdojo-api-generated/actions/workflows/test.yml/badge.svg)](https://github.com/fopina/defectdojo-api-generated/actions/workflows/test.yml)
[![codecov](https://codecov.io/github/fopina/defectdojo-api-generated/graph/badge.svg)](https://codecov.io/github/fopina/defectdojo-api-generated)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/defectdojo-api-generated.svg)](https://pypi.org/project/defectdojo-api-generated/)
[![Current version on PyPi](https://img.shields.io/pypi/v/defectdojo-api-generated)](https://pypi.org/project/defectdojo-api-generated/)
[![Very popular](https://img.shields.io/pypi/dm/defectdojo-api-generated)](https://pypistats.org/packages/defectdojo-api-generated)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Python library to interact with DefectDojo - generated from OpenAPI definition using https://openapi-generator.tech/

Multiple changes done on top of default openapi-generator:
* A friendlier Client class
* Tweak validations to reduce package import time to about 1/3
* Remove most of pydantic/schema validations due to inconsistencies with actual database schema/requirements (tracked in https://github.com/fopina/defectdojo-api-generated/issues/39)
* *Iterator* methods for every *list* API method to handle pagination automatically
* A nice CLI exposing all the API methods <3
  * published as a separate package, to keep library-only installs free of console-script conflicts

## Example

### Library

```
pip install defectojo-api-generated
```

<!-- example-id: example.py -->
```python
    from defectdojo_api_generated import DefectDojo

    # password publicly available in https://github.com/DefectDojo/django-DefectDojo/?tab=readme-ov-file#demo
    dojo = DefectDojo(base_url='https://demo.defectdojo.org/', auth=('admin', PASSWORD))
    for ind, finding in enumerate(dojo.findings_api.list_iterator(title='Stored XSS')):
        if not ind:
            print(f'Total matched findings: {finding.page.count}')
        print(f'- [{finding.result.severity}] {finding.result.title} - {finding.result.description}')
    r = dojo.system_settings_api.list(limit=1)
    print(f'- {r.results[0]}')
```

#### **Full documentation** [readthedocs](https://defectdojo-api-generated.readthedocs.io/)

### CLI

[![asciicast](https://asciinema.org/a/fIPDy8iYxGL85pXb.svg)](https://asciinema.org/a/fIPDy8iYxGL85pXb)

> [uv](https://docs.astral.sh/uv/) recommended or [pipx](https://github.com/pypa/pipx)

```
uv tool install defectdojo-api-generated-cli
```

```
$ dojo 
Usage: dojo [OPTIONS] COMMAND [ARGS]...

  DefectDojo CLI

Options:
  ...
Commands:
  api     Interact directly with any API/method
  config  Show or edit the current CLI configuration
  status  Quick connectivity check
```

You can also skip tool install and just run it with:

```
$ uvx defectdojo-api-generated-cli
Usage: dojo [OPTIONS] COMMAND [ARGS]...
...
```

## Contributing

Check out [CONTRIBUTING.md](CONTRIBUTING.md)

## API notes

### Required properties

DefectDojo's OpenAPI schema and actual database/API validations are inconsistent in some places, so this library assumes all properties as **not required** skipping client-side validation and delegating those validations to server.

Refer to https://github.com/fopina/defectdojo-api-generated/issues/31 and https://github.com/fopina/defectdojo-api-generated/issues/39 for more details / reasoning.

### Server versions

This library is versioned after the OpenAPI schema version (DefectDojo version) it was generated against, eg: when re-generated against DefectDojo *2.57.0* schema, it will be released as *2.57.0*

Any changes done to the package (such as packaging metadata or extra schema tweaks), while on the same schema version, will be released as `post` fixes, eg: *2.57.0.post1*

Given the very few validations kept (previous note), there might be no issue using "latest" version of this package against an older DefectDojo. However, if there is any, just install the closest matching version.
