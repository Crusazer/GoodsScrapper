#!/bin/sh
sleep 3
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput || true
python manage.py runserver 0.0.0.0:8000