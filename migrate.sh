#!/usr/bin/env bash

set -e

pushd devtest

python manage.py makemigrations actions
python manage.py makemigrations pledges

python manage.py migrate

popd
