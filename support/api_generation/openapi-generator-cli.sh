#!/bin/sh

IMAGE=${OPENAPITOOLS_IMAGE:-openapitools/openapi-generator-cli:v7.12.0}

echo $IMAGE


VOL=$(cd $(dirname $0); cd ..; cd ..; pwd)

docker run --rm -e https_proxy -e http_proxy -e no_proxy -v $VOL:/local $IMAGE "$@"
