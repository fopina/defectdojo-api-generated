#!/bin/sh

set -eo pipefail

# make sure we're on root dir
cd $(dirname $0)
cd ..
cd ..

./support/openapi/tweak_openapi.py

./support/api_generation/openapi-generator-cli.sh \
                           generate \
                           -i support/openapi/build/openapi.json \
                           -c support/api_generation/config.yaml \
                           -o .

rm -fr tests/generated
mv defectdojo_api_generated/test tests/generated
