#!/usr/bin/env bash

# exit on first error
set -xe

# create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install (or update) requirements
python -m pip install -r requirements.txt
python -m pip install -r requirements-otel.txt

# run migrations
./manage.py migrate

# Start redis server
redis-server &

# Run Django application on localhost:8090
./manage.py runserver 0.0.0.0:8090
#gunicorn movie_search.project.asgi:application -k uvicorn.workers.UvicornWorker