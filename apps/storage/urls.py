"""Storage URLs"""
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('<str:key>', views.index, name='index'),
]

app_name = 'storage'
