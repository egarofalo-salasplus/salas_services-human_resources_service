#!/bin/sh

# Salir si ocurre algún error
set -e

# Ejecutar migraciones
python manage.py migrate

# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Iniciar el servidor
gunicorn --bind 0.0.0.0:8000 human_resources_service.wsgi:application
