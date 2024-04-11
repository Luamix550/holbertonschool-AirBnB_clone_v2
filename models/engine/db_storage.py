#!/usr/bin/python3
""" State Module for HBNB project """
from MySQLdb import _mysql
import os
from models.engine import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

class DBStorage():
        __engine =  None
        __session = None

        def __init__(self):
                user = os.getenv("HBNB_MYSQL_USER")
                password = os.getenv("HBNB_MYSQL_PWD")
                host = os.getenv("HBNB_MYSQL_HOST9", default="localhost")
                database = os.getenv("HBNB_MYSQL_DB")

                self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                user, password, database), pool_pre_ping=True)

                Base.metadata.create_all(self.__engine)

                Session = sessionmaker(bind=self.__engine)
                session = Session()
