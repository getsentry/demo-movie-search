#!/usr/bin/env bash

# exit on first error
set -xe

# create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install (or update) requirements
python -m pip install -r requirements-otel.txt

# run migrations
# ./manage.py migrate

# Start redis server
redis-server &

cd movie_search

# Install otel auto instrumentation
#opentelemetry-bootstrap -a install

# Run Django application on localhost:8000 instrumented by otel
# - runserver
# DJANGO_SETTINGS_MODULE=project.settings OTEL_METRICS_EXPORTER=none opentelemetry-instrument \
#     --traces_exporter console \
#     --metrics_exporter console \
#     python manage.py runserver 0.0.0.0:8090 --noreload
export DJANGO_SETTINGS_MODULE=project.settings
opentelemetry-instrument -e none \
    python manage.py runserver 0.0.0.0:8090 --noreload

# - gunicorn
# DJANGO_SETTINGS_MODULE=project.settings OTEL_METRICS_EXPORTER=none opentelemetry-instrument \
#     --traces_exporter console \
#     --metrics_exporter console \
#     gunicorn --bind 0.0.0.0:8090 --workers 1 --threads 8 project.wsgi:application

# - uwsgi
# DJANGO_SETTINGS_MODULE=project.settings OTEL_METRICS_EXPORTER=none opentelemetry-instrument \
#     --traces_exporter console \
#     --metrics_exporter console \
#     uwsgi --http :8090 --module project.wsgi
# DJANGO_SETTINGS_MODULE=project.settings opentelemetry-instrument \
#     uwsgi --http :8090 --enable-threads --module project.wsgi


# DJANGO_SETTINGS_MODULE=project.settings OTEL_METRICS_EXPORTER=none \
#     python manage.py runserver 0.0.0.0:8090 --noreload    