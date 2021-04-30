"""
ASGI config for keyval_storage project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
import apps.storage.routing

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            apps.storage.routing.websocket_urlpatterns
        )
    ),
})
