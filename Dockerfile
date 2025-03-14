# TODO: remove all file if no docker image is required (ie: just a python library)
FROM python:3.10-alpine AS base

# --- builder
FROM base AS builder
WORKDIR /app
WORKDIR /

COPY Pipfile.lock .
RUN pip install pipenv
RUN pipenv requirements > requirements.txt
RUN pip install --target=/app -r requirements.txt

# --- main
FROM base
COPY --from=builder /app /app
ENV PYTHONPATH=/app
# TODO: replace with your package name
COPY example /app/example

ENTRYPOINT ["python3", "-m", "example"]
