# defectdojo-api-generated

[![ci](https://github.com/fopina/defectdojo-api-generated/actions/workflows/publish-main.yml/badge.svg)](https://github.com/fopina/defectdojo-api-generated/actions/workflows/publish-main.yml)
[![test](https://github.com/fopina/defectdojo-api-generated/actions/workflows/test.yml/badge.svg)](https://github.com/fopina/defectdojo-api-generated/actions/workflows/test.yml)
[![codecov](https://codecov.io/github/fopina/defectdojo-api-generated/graph/badge.svg)](https://codecov.io/github/fopina/defectdojo-api-generated)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/defectdojo-api-generated.svg)](https://pypi.org/project/defectdojo-api-generated/)
[![Current version on PyPi](https://img.shields.io/pypi/v/defectdojo-api-generated)](https://pypi.org/project/defectdojo-api-generated/)
[![Very popular](https://img.shields.io/pypi/dm/defectdojo-api-generated)](https://pypistats.org/packages/defectdojo-api-generated)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Python library to interact with DefectDojo - generated from OpenAPI definition using https://openapi-generator.tech/

## Install

```
pip install defectojo-api-generated
```

## Usage

```python
from defectdojo_api_generated import DefectDojo

# password publicly available in https://github.com/DefectDojo/django-DefectDojo/?tab=readme-ov-file#demo
# then get API token from https://demo.defectdojo.org/api/key-v2
dojo = DefectDojo('https://demo.defectdojo.org/', token=...)
r = dojo.findings_api.list()
print(r.json())
```

## Build

Check out [CONTRIBUTING.md](CONTRIBUTING.md)

## API notes

### Required properties

DefectDojo's OpenAPI schema and actual database/API validations are inconsistent in some places, so this library assumes all properties as **not required** skipping client-side validation and delegating those validations to server.

Refer to https://github.com/fopina/defectdojo-api-generated/issues/31 and https://github.com/fopina/defectdojo-api-generated/issues/39 for more details / reasoning.

### Server versions

This library is versioned after the OpenAPI schema version (DefectDojo version) it was generated against, eg: when re-generated against DefectDojo *2.57.0* schema, it will be released as *2.57.0*

Any changes done to the package (such as packaging metadata or extra schema tweaks), while on the same schema version, will be released as `post` fixes, eg: *2.57.0.post1*

Given the very few validations kept (previous note), there might be no issue using "latest" version of this package against an older DefectDojo. However, if there is any, just install the closest matching version.
