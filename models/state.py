#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'States'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="State", cascade="Delete")

    @property
    def get_cities(self):
        city_instances = []
        for City in self.cities:
            if City.state_id == State.id:
                city_instances.append(City)
        return city_instances
