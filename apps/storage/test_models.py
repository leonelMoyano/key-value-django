"""Test module for models, focused on model behaviour and expected constraints"""
import unittest

import pytest
from django.db.utils import IntegrityError

from .models import KeyValuePair


class KeyValuePairTest(unittest.TestCase):
    """Key Value model tests"""

    @pytest.mark.django_db(transaction=True)
    def test_cant_repeat_key(self):
        """KeyValue can't repeat keys"""
        test_key = 'key_example_dup'
        KeyValuePair.objects.create(key=test_key, value='1')
        self.assertRaises(IntegrityError, KeyValuePair.objects.create, key=test_key, value='2')
