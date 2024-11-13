import io
import os
import django
from django.core.management import call_command

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MateusGurzaCrud.settings')

# Initialize Django
django.setup()

# Dump data to a JSON file
with io.open('data.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', '--natural-primary', '--natural-foreign',
                 '--exclude', 'contenttypes', '--exclude', 'auth.Permission',
                 stdout=f)