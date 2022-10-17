#!/usr/bin/env bash

# exit on first error
set -xe

# create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install (or update) requirements
pip install -r requirements.txt

# Start redis server
redis-server &

# Run FastAPI application on localhost:8000
uvicorn main:app --reload
