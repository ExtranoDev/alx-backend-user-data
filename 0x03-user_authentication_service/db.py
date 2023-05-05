#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self):
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """"save the user to the database
            and returns user object"""
        sess_usr = User(email=email, hashed_password=hashed_password)
        self._session.add(sess_usr)
        self._session.commit()
        return sess_usr

    def find_user_by(self, **kwargs) -> User:
        """takes in arbitrary keyword arguments
            returns the first row found in the users table
            filtered by the method’s input arguments
        """
        if kwargs is None:
            raise InvalidRequestError
        for key in kwargs.keys():
            if not hasattr(User, key):
                raise InvalidRequestError

        try:
            user = self._session.query(User).filter_by(**kwargs).first()
        except InvalidRequestError:
            raise InvalidRequestError
        if user is None:
            raise NoResultFound
        else:
            return user
