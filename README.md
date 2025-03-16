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
r = dojo.findings_api.findings_list()
print(r.json())
```

## Build

Check out [CONTRIBUTING.md](CONTRIBUTING.md)
