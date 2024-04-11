#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.engine import Base
from sqlalchemy import create_engine
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
        host = os.getenv("HBNB_MYSQL_HOST", default="localhost")
        database = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, password, host, database),
            pool_pre_ping=True,
        )

        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def new(self, obj):
        with Session(self.__engine):
            self.__session.add(self.__session)

    def save(self):
        with Session(self.__engine):
            self.__session.commit()

    def delete(self, obj=None):
        if obj is None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def all(self, cls=None):
        new_dict = {}

        if cls is None:
            classes = [User, Place, State, City, Amenity, Review]

            for c in classes:
                objs = self.__session.query(c).all()

                for obj in objs:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    new_dict[key] = obj
        else:
            objs = self.__session.query(cls).all()

            for obj in objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                new_dict[key] = obj
        return new_dict
