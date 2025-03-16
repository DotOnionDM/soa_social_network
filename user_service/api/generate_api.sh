sudo rm -Rf ./openapi-generator-output
docker run --rm -v "${PWD}":/app openapitools/openapi-generator-cli:latest-release generate  \
    -i /app/spec.yml  -g python-fastapi   -o /app/openapi-generator-output 
