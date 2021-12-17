#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable = False)
    cities = relationship(
        "City",
        cascade = "all, delete, delete-orphan",
        back_populates = "state"
    )
