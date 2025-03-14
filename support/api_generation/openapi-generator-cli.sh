#!/bin/sh

IMAGE=openapitools/openapi-generator-cli:v7.12.0

VOL=$(cd $(dirname $0); cd ..; cd ..; pwd)

docker run --rm -v $VOL:/local $IMAGE "$@"
