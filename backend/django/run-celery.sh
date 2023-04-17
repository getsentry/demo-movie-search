#!/usr/bin/env bash

# exit on first error
set -xe

# create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install (or update) requirements
python -m pip install -r requirements.txt

# run migrations
./manage.py migrate

# Start redis server
redis-server &

# Run Celery beat and workers
cd movie_search
export DJANGO_SETTINGS_MODULE=project.settings
celery -A project.celery worker -B --loglevel=DEBUG --concurrency=1