import sys
import os

# Make the Django project importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabanafish.settings')

import django
django.setup()

# Run migrations automatically on cold start (Vercel serverless)
from django.core.management import call_command
try:
    call_command('migrate', '--run-syncdb', verbosity=0)
except Exception:
    pass

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()

# Vercel expects a variable named "handler" or "app"
handler = app
