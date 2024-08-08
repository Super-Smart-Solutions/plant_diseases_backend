#!/bin/bash

# Start the FastAPI app using Docker Compose
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up --build -d

# Wait for the app to start
sleep 20

# Download the OpenAPI JSON file
curl -o api_doc.json http://0.0.0.0:8000/api/openapi.json

# Stop the FastAPI app
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . down

# Install Redoc CLI
npm install -g redoc-cli

# Generate Redoc HTML
mkdir -p docs
npx @redocly/cli build-docs api_doc.json -o docs/index.html