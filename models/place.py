#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models import storage

Base = declarative_base()

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"), primary_key=True),
    Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True),
)


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"
    id = Column(String(60), nullable=False, primary_key=True)
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
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)

    @property
    def amenities(self):
        amenity_instances = []
        for amenity in storage.all(amenity).values():
            if amenity.id == Place.amenity_ids:
                amenity_instances.append(amenity)
        return amenity_instances

    @amenities.setter
    def amenities(self, value):
        if isinstance(value, Amenity):
            self.amenity_ids.append(value.id)
