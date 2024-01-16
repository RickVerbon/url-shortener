#!/bin/bash

# Apply database migrations
python manage.py makemigrations
python manage.py migrate


# Start the Gunicorn server
exec gunicorn urlshortener.wsgi:application --bind 0.0.0.0:8000
