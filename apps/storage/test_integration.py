"""Test module for integration tests, focused on test that utilize both WS and HTTP services"""
import json

import pytest
from asgiref.sync import sync_to_async
from channels.testing import WebsocketCommunicator
from django.test import Client

from .consumers import StorageConsumer


@pytest.mark.django_db(transaction=True)
@pytest.mark.asyncio
async def test_storage_consumer_save_and_read():
    """Key value is saved through WS and read through HTTP"""
    test_key, test_value = 'key_example_ws', 'value_example'
    communicator = WebsocketCommunicator(StorageConsumer.as_asgi(), '/ws/storage/')
    connected, _ = await communicator.connect()
    assert connected, 'Websocket connection could not be established'
    await communicator.send_to(text_data=f'{{"key":"{test_key}","value":"{test_value}"}}')
    await communicator.receive_from()
    client = Client()
    response = await sync_to_async(client.get)(f'/storage/{test_key}',)
    assert response.status_code == 200, 'Reading back stored keyvalue should return 200'
    assert json.loads(response.content) == {
        'key': test_key,
        'value': test_value,
        'message': '',
        'status': 200
    }, 'Reading back stored keyvalue response does not match expected result'
    await communicator.disconnect()


@pytest.mark.django_db(transaction=True)
@pytest.mark.asyncio
async def test_storage_consumer_can_update():
    """Key value is saved through WS, updated and read through HTTP"""
    test_key, test_value = 'key_example_ws_update', 'value_example'
    new_value = test_value + 'new_value'
    communicator = WebsocketCommunicator(StorageConsumer.as_asgi(), '/ws/storage/')
    connected, _ = await communicator.connect()
    assert connected, 'Websocket connection could not be established'
    await communicator.send_to(text_data=f'{{"key":"{test_key}","value":"{test_value}"}}')
    await communicator.receive_from()
    await communicator.send_to(text_data=f'{{"key":"{test_key}","value":"{new_value}"}}')
    await communicator.receive_from()
    await communicator.disconnect()
    client = Client()
    response = await sync_to_async(client.get)(f'/storage/{test_key}',)
    assert response.status_code == 200, 'Reading back stored keyvalue should return 200'
    assert json.loads(response.content) == {
        'key': test_key,
        'value': new_value,
        'message': '',
        'status': 200
    }, 'Reading back stored keyvalue response does not match expected result'
