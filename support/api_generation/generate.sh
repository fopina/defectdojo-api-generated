#!/bin/sh

set -eo pipefail

TEMPDIR=apiclient.spec

# make sure we're on root dir
cd $(dirname $0)
cd ..
cd ..

rm -fr $TEMPDIR

# add custom templates to full templates
cp -r ./support/api_generation/custom_templates/ ./support/api_generation/templates.spec/
./support/api_generation/openapi-generator-cli.sh \
                           generate \
                           -i 'https://defectdojo.eng.netsuite.com/api/v2/oa3/schema/?format=json' \
                           -g python \
                           -c /local/support/api_generation/config.yaml \
                           --template-dir /local/support/api_generation/templates.spec \
                           -o /local/$TEMPDIR/

rm -fr defectdojo_cli/api_generated
mv $TEMPDIR/defectdojo_cli/api_generated defectdojo_cli/
mv $TEMPDIR/defectdojo_cli/api_generated_README.md defectdojo_cli/api_generated/
