#!/usr/bin/python3
""" """
import os

from tests.test_models.test_base_model import TestBasemodel
from models.city import City


class TestCity(TestBasemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.name), str)
