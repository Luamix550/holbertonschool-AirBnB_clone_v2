#!/usr/bin/python3
""" State Module for HBNB project """
from MySQLdb import _mysql
import os
from models.engine import Base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session, sessionmaker, scoped_session

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

		if os.getenv("HBNB_ENV") == "test":
			Base.metadata.drop_all(self.__engine)

		def new(self, obj):
			with Session(self.__engine):
				session.add(self.__session)

		def save(self):
			with Session(self.__engine):
				session.commit()

		def delete(self, obj=None):
			if obj is None:
				session.delete(obj)

		def reload(self):
			Base.metadata.create_all(self.__engine)
			session_factory = sessionmaker(
			bind=self.__engine, expire_on_commit=False)
			Session = scoped_session(session_factory)
			self.__session = Session()
