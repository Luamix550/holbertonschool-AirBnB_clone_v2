#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, ForeignKey, Integer, Float

Base = declarative_base()


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=True)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=True)
    name = Column(String(128), nullable=True)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=True)
    number_bathrooms = Column(Integer, default=0, nullable=True)
    max_guest = Column(Integer, default=0, nullable=True)
    price_by_night = Column(Integer, default=0, nullable=True)
    latitude = Column(Float, default=0, nullable=True)
    longitude = Column(Float, default=0, nullable=True)
    amenity_ids = []
