#!/bin/sh


echo "Waiting for postgres..."

while ! nc -z db $DB_PORT; do
    sleep 0.1
done

echo "PostgreSQL started"

poetry run python manage.py migrate --noinput
echo "run migrations"

if [ "$DEBUG" = "False" ]
then
poetry run python manage.py collectstatic --noinput
echo "colleted static files"

exec gunicorn core.wsgi:application --bind ${RUN_HOST}:${RUN_PORT}
else
  exec poetry run python manage.py runserver ${RUN_HOST}:${RUN_PORT}
fi