# python package template

## Content

* `pytest` for tests: `make test`
* `ruff` for linting/formatting: `make lint` (replaces both `black` and `isort`)
* [pyproject-pipenv](https://github.com/fopina/pyproject-pipenv) to make sure dependencies in pyproject.toml and Pipfile are in sync
* `.github` with actions ready to be used
    * [test](.github/workflows/test.yml) runs lint checks, unit tests and pyproject-pipenv
    * [publish-dev](.github/workflows/publish-dev.yml) publishes feature branches (`dev`/`dev-*`) to:
      * [testpypi](https://test.pypi.org) - more about this on [Notes](#feature-branch-publishing)
      * docker image to ghcr.io - remove job if image makes no sense
    * [publish-main](.github/workflows/publish-main.yml) publishes semver tags to:
      * [pypi](https://pypi.org)
      * docker image to ghcr.io

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

## Notes

### Feature branch publishing

`publish-dev` workflow publishes `dev`/`dev-*` branches to [testpypi](https://test.pypi.org).

Other common approach to publish dev branches is to use pre-release channels: version the package with a `rc` or `beta` suffix (such as `1.0.0-beta1`) and pypi will consider pre-release. In order to install this, the user needs to do `pip install PACKAGE --pre` otherwise the latest stable is picked up.  
However this will "pollute" your pypi index and it still requires you to bump the version (`1.0.0-beta1` < `1.0.0`) or to install the branch using specific version.

Yet another approach is to simply use an entirely different package name for the dev releases. Tensorflow does that, for example, with [tf-nightly](https://pypi.org/project/tf-nightly/).

## ---

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
