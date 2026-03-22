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
                           --remove-operation-id-prefix \
                           -c support/api_generation/config.yaml \
                           -o .

rm -fr tests/generated
mkdir -p tests/generated
mv defectdojo_api_generated/test/* tests/generated/
rm -fr docs/apimodels/
mkdir -p docs
mv defectdojo_api_generated/docs/ docs/apimodels/
# not using -i to work on both macOS and linux
sed -e 's#(defectdojo_api_generated/docs/#(apimodels/#g' defectdojo_api_generated_README.md > docs/README.md
rm defectdojo_api_generated_README.md
