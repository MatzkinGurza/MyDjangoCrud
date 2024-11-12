#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py migrate  # Adiciona as migrações do banco de dados
python manage.py collectstatic --no-input