#!/bin/bash
# written by Copilot

set -eo pipefail

cd $(dirname $0)

COMPOSE_FILE="docker-compose.yml"
SERVICE_URL="http://localhost:8080"
TIMEOUT=300
INTERVAL=2
export DJANGO_VERSION="2.46.2"
export NGINX_VERSION="${DJANGO_VERSION}"

# Start docker compose in detached mode
docker compose -f "$COMPOSE_FILE" up -d

echo "Waiting for service to be ready at $SERVICE_URL..."

SECONDS=0
while (( SECONDS < TIMEOUT )); do
    STATUS=$(curl -s -o /dev/null -Lw "%{http_code}" "$SERVICE_URL" || true)
    if [[ "$STATUS" == "200" ]]; then
        echo "Service is ready!"
        exit 0
    fi
    # echo "NOT READY: status $STATUS"
    sleep $INTERVAL
done

echo "Service did not become ready within $TIMEOUT seconds."
exit 1