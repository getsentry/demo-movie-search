#!/usr/bin/env bash

# exit on first error
set -xe

# create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install (or update) requirements
python -m pip install -r requirements.txt

# Start fresh redis server
pkill redis-server || true
sleep 1
rm -rf dump.rdb
redis-server --daemonize yes

# run migrations
./manage.py migrate

# Run Django application on localhost:8000
./manage.py runserver 0.0.0.0:8000
# cd movie_search && gunicorn project.asgi:application -k uvicorn.workers.UvicornWorker && cd -
# cd movie_search && mprof run --multiprocess --output "./mprofile_$(date +%Y%m%d%H%M%S).dat" gunicorn project.wsgi:application && cd -