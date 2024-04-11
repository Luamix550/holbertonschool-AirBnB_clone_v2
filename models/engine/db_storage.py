#!/usr/bin/python3
""" State Module for HBNB project """
from MySQLdb import _mysql
import os
from models.engine import Base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session, sessionmaker, scoped_session

from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST9", default="localhost")
        database = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(user, password, database),
            pool_pre_ping=True,
        )

        Base.metadata.create_all(self.__engine)

                Session = sessionmaker(bind=self.__engine)
                session = Session()
