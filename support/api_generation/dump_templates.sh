#!/bin/sh

set -eo pipefail

# helper to dump current templates (examples for custom templates) - relative to root
TEMPDIR=support/api_generation/templates.spec

cd $(dirname $0)
cd ..
cd ..

rm -fr $TEMPDIR

./support/api_generation/openapi-generator-cli.sh author template \
                           -g python \
                           --output $TEMPDIR
