#!/usr/bin/env bash

set -e

pushd devtest

# Remove any existing database
rm -f db.sqlite3

# Re-create the database
python manage.py migrate

# Create an admin user
export DJANGO_SUPERUSER_PASSWORD="admin"
python manage.py createsuperuser --no-input --username admin --email admin@example.com

# Populate the database
python manage.py runscript populate_data

popd
