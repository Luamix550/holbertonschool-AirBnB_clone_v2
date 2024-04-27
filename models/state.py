#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="State", cascade="delete")

    @property
    def cities(self):
        """
        Getter method to return the list of City objects associated with this State.
        """
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            return self.cities
        else:
            from models import storage
            from models.city import City
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
