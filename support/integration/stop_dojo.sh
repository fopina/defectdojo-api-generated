#!/bin/bash
# written by Copilot

set -eo pipefail

cd $(dirname $0)

COMPOSE_FILE="docker-compose.yml"

docker compose -f "$COMPOSE_FILE" down
