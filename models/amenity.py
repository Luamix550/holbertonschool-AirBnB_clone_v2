#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Table, ForeignKey, relationship

Base = declarative_base()

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"), primary_key=True),
    Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True),
)


class Amenity(BaseModel):
    __tablename__ = "amenities"
    name = Column(String(128), nullable=True)
    place_amenities = relationship(
        "Place", secondary=place_amenity, backref="amenities"
    )
