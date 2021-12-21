#!/usr/bin/python3
""" """
import os

from tests.test_models.test_base_model import TestBasemodel
from models.place import Place


class TestPlace(TestBasemodel):
    """Represents the tests for the Place model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Tests the type of city_id."""
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Tests the type of user_id."""
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Tests the type of name."""
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.name), str)

    def test_description(self):
        """Tests the type of description."""
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Tests the type of number_rooms."""
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Tests the type of number_bathrooms."""
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Tests the type of max_guest."""
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Tests the type of price_by_night."""
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Tests the type of latitude."""
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Tests the type of longitude."""
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """Tests the type of amenity_ids."""
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.amenity_ids), list)
