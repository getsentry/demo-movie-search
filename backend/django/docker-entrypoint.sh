#!/bin/bash
set -xe

# run migrations
DEBUG=True ./manage.py migrate --no-input && ./manage.py initadmin

# execute the given command
exec "$@"
