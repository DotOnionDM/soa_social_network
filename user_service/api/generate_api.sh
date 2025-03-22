#!/bin/sh

set -e
ROOT=$(dirname $0)
cd "$ROOT"

sudo rm -Rf ./openapi-generator-output
docker run --rm -v "${PWD}":/app openapitools/openapi-generator-cli:latest-release generate  \
    -i /app/spec.yaml  -g python-fastapi   -o /app/openapi-generator-output \
    --additional-properties=packageName=user_service_base --additional-properties=fastapiImplementationPackage=user_service_impl
