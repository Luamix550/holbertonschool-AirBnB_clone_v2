#!/usr/bin/python3
""" State Module for HBNB project """
from MySQLdb import _mysql
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBStorage():
        __engine =  None
        __session = None

        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST9", default="localhost")
        database = os.getenv("HBNB_MYSQL_DB")

        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, password, database), pool_pre_ping=True)

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        
