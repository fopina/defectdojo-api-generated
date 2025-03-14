# WIP

* Map versions to Dojo version - use postfixes for non-schema changes (such as templating or similar)
* 

## New project checklist

* [ ] Replace folder `example` with the actual package
* [ ] Replace `LICENSE` if MIT does not apply
* [ ] Search the project for `# TODO` to find the (minimum list of) places that need to be changed.
* [ ] Add PYPI credentials to secrets
    * `PYPI_USERNAME` and `PYPI_TOKEN` to publish tags to pypi
    * `TESTPYPI_USERNAME` and `TESTPYPI_TOKEN` to publish dev branches to testpypi
* [ ] Add [codecov](https://app.codecov.io/github/fopina/) token
    * `CODECOV_TOKEN` taken from link above
* [ ] Replace this README.md - template below

# fp-github-template-example

[![ci](https://github.com/fopina/python-package-template/actions/workflows/publish-main.yml/badge.svg)](https://github.com/fopina/python-package-template/actions/workflows/publish-main.yml)
[![test](https://github.com/fopina/python-package-template/actions/workflows/test.yml/badge.svg)](https://github.com/fopina/python-package-template/actions/workflows/test.yml)
[![codecov](https://codecov.io/github/fopina/python-package-template/graph/badge.svg)](https://codecov.io/github/fopina/python-package-template)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/fp-github-template-example.svg)](https://pypi.org/project/fp-github-template-example/)
[![Current version on PyPi](https://img.shields.io/pypi/v/fp-github-template-example)](https://pypi.org/project/fp-github-template-example/)
[![Very popular](https://img.shields.io/pypi/dm/fp-github-template-example)](https://pypistats.org/packages/fp-github-template-example)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

CLI that echos whatever you tell it to.

## Install

```
pip install fp-github-template-example
```

## Usage

```
$ example-cli
Got nothing to say?

$ example-cli hello
HELLO right back at ya!
```

```python
>>> from example import demo
>>> demo.echo('ehlo')
'EHLO right back at ya!'
```

## Build

Check out [CONTRIBUTING.md](CONTRIBUTING.md)
