#!/usr/bin/python3

""" The State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """The amenity class, contains name field and places relationship.
    """
    __tablename__ = "amenities"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column('name', String(128), nullable=False)
        place_amenity = relationship('Place',
                                     secondary='place_amenity',
                                     back_populates='amenities')
    else:
        name = ""
