"""
ASGI config for ai_blog_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
import os

from django.core.asgi import get_asgi_application

settings_module = 'ai_blog_app.deployment_settings' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'ai_blog_app.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE',settings_module )

application = get_asgi_application()