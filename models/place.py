#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table

from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        nullable=False
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        nullable=False
    )
)
"""Represents the many to many relationship table \
between Place and Amenity records.
"""


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    user = relationship(
        'User',
        back_populates='places'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    cities = relationship(
        'City', back_populates='places'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    reviews = relationship(
        'Review',
        cascade="all, delete, delete-orphan",
        back_populates='place'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    amenities = relationship(
        'Amenity',
        secondary=place_amenity,
        viewonly=False,
        back_populates='place_amenities'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None

    @property
    def reviews(self):
        """Returns the reviews of this Place"""
        from models import storage
        reviews_of_place = []
        for value in storage.all(Review).values():
            if value.place_id == self.id:
                reviews_of_place.append(value)
        return reviews_of_place

    @property
    def amenities(self):
        """Returns the amenities of this Place"""
        from models import storage
        amenities_of_place = []
        for value in storage.all(Amenity).values():
            if value.id in self.amenity_ids:
                amenities_of_place.append(value)
        return amenities_of_place

    @amenities.setter
    def amenities(self, value):
        """Adds an amenity to this Place"""
        if type(value) is Amenity:
            if value.id not in self.amenity_ids:
                self.amenity_ids.append(value.id)
