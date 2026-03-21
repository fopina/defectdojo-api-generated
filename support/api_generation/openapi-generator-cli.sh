#!/bin/sh

IMAGE=${OPENAPITOOLS_IMAGE:-openapitools/openapi-generator-cli:v7.20.0}

VOL=$(cd $(dirname $0); cd ..; cd ..; pwd)

docker run --rm \
    -e https_proxy \
    -e http_proxy \
    -e no_proxy \
    -e JAVA_OPTS="-Dlog.level=warn" \
    -v $VOL:$VOL \
    -w $PWD \
    $IMAGE "$@"
