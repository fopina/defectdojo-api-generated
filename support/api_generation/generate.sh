#!/bin/sh

set -eo pipefail

OPENAPI_PATH=${OPENAPI_PATH:-"/local/support/openapi.json"}

# make sure we're on root dir
cd $(dirname $0)
cd ..
cd ..

# add custom templates to full templates
cp -r ./support/api_generation/custom_templates/ ./support/api_generation/templates.spec/
./support/api_generation/openapi-generator-cli.sh \
                           generate \
                           -i "${OPENAPI_PATH}" \
                           -c /local/support/api_generation/config.yaml \
                           -o /local/

rm -fr tests/generated
mv defectdojo_api_generated/test tests/generated
