#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """"save the user to the database
            and returns user object"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """takes in arbitrary keyword arguments
            returns the first row found in the users table
            filtered by the method’s input arguments
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound
            return user
        except AttributeError:
            raise InvalidRequestError

    def update_user(self, user_id: int, **kw) -> None:
        """implements the update_user method
        takes a required user_id integer
        arbitrary keyword arguments, and returns None
        """
        try:
            user = self.find_user_by(id=user_id)
        except NoResultFound:
            raise ValueError

        try:
            for key, value in kw.items():
                if hasattr(User, key):
                    setattr(user, key, value)
                else:
                    raise ValueError
        except ValueError:
            raise ValueError
        self._session.commit()
        return None
