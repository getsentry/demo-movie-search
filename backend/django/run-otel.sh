#!/usr/bin/env bash

# exit on first error
set -xe

# create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install (or update) requirements
python -m pip install -r requirements-otel.txt

# run migrations
./manage.py migrate

# Start redis server
redis-server &

cd movie_search

# Install otel auto instrumentation
opentelemetry-bootstrap -a install

# Run Django application on localhost:8000 instrumented by otel
export DJANGO_SETTINGS_MODULE=project.settings
export OTEL_METRICS_EXPORTER=none
opentelemetry-instrument \
    --traces_exporter console \
    python manage.py runserver --noreload
