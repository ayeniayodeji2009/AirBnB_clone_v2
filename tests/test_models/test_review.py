#!/usr/bin/python3
""" """
import os

from tests.test_models.test_base_model import TestBasemodel
from models.review import Review


class TestReview(TestBasemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.text), str)
