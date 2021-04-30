"""Storage WS consumers"""
from channels.generic.websocket import JsonWebsocketConsumer
from .models import KeyValuePair


class StorageConsumer(JsonWebsocketConsumer):
    """Websocket consumer for storage communication"""
    def connect(self):
        self.accept()

    def receive_json(self, content, **kwargs):
        """Create or update KeyValuePair on recieving ws message"""
        obj, created = KeyValuePair.objects.update_or_create(
            key=content['key'],
            defaults={'value': content['value']},
        )
        self.send_json({
            'message': obj.key + ' created' if created else ' updated',
            'status': 200
        })
