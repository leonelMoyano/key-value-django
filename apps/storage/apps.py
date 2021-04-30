"""Storage app config"""
from django.apps import AppConfig


class StorageConfig(AppConfig):
    """Config values as expected by Django"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.storage'
