"""Test module for views"""
import json
import unittest

import pytest
from django.test import Client


class StorageIntegrationTest(unittest.TestCase):
    """HTTP endpoint tests"""

    @pytest.mark.django_db(transaction=True)
    def test_404_on_unexisting_keyvalue(self):
        """404 response on querying for unexisting key"""
        non_existing_key = 'non_existing_key'
        client = Client()
        response = client.get(f'/storage/{non_existing_key}', )
        self.assertEqual(response.status_code, 404,
                         msg='Attempting to read unexisting keyvalue should return 404')
        self.assertEqual(json.loads(response.content), {
            'message': f'No value found for key {non_existing_key}',
            'status': 404
        }, msg='Reading back stored keyvalue response does not match expected result')
