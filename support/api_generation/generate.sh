#!/bin/sh

set -eo pipefail

TEMPDIR=apiclient.spec
OPENAPI_PATH=${OPENAPI_PATH:-"https://demo.defectdojo.org/api/v2/oa3/schema/?format=json"}

# make sure we're on root dir
cd $(dirname $0)
cd ..
cd ..

rm -fr $TEMPDIR

# add custom templates to full templates
cp -r ./support/api_generation/custom_templates/ ./support/api_generation/templates.spec/
./support/api_generation/openapi-generator-cli.sh \
                           generate \
                           -i "${OPENAPI_PATH}" \
                           -g python \
                           -c /local/support/api_generation/config.yaml \
                           --template-dir /local/support/api_generation/templates.spec \
                           -o /local/$TEMPDIR/

rm -fr defectdojo_api_generated
mv $TEMPDIR/defectdojo_api_generated .
