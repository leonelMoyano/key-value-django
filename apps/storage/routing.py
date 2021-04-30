"""Routing module for WS channels configuration"""
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path('ws/storage/', consumers.StorageConsumer.as_asgi()),
]
