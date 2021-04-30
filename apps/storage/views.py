"""Storage views"""
from django.http.response import JsonResponse
from .models import KeyValuePair


def index(request, key):
    """"Lookup KeyValuePair on key identifier, return 404 if not found"""
    try:
        key_value = KeyValuePair.objects.get(key=key)
        return JsonResponse(data={
            'key': key_value.key,
            'value': key_value.value,
            'message': '',
            'status': 200,
        }, status=200)
    except KeyValuePair.DoesNotExist:
        return JsonResponse(data={
            'message': f'No value found for key {key}',
            'status': 404,
        }, status=404)
