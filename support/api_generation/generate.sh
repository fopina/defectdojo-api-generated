#!/bin/sh

set -eo pipefail

OPENAPI_PATH=${OPENAPI_PATH:-"support/openapi.json"}

# make sure we're on root dir
cd $(dirname $0)
cd ..
cd ..

./support/api_generation/openapi-generator-cli.sh \
                           generate \
                           -i "${OPENAPI_PATH}" \
                           -c support/api_generation/config.yaml \
                           -o .

rm -fr tests/generated
mv defectdojo_api_generated/test tests/generated
