"""Storage models"""
from django.db import models


class KeyValuePair(models.Model):
    """Key Value pair where key is the unique identifier"""
    key = models.CharField(max_length=100, primary_key=True)
    value = models. CharField(max_length=100)
