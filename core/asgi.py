"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

try:
    from core.env import env
    settings_module = env('DJANGO_SETTINGS_MODULE', default='core.settings.local')
except (ImportError, NameError):
    settings_module = 'core.settings.local'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_asgi_application()
