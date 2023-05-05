#!/usr/bin/env python3
"""
Hash User password
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Helps hash a password
    """
    password = password.encode('utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_pass = _hash_password(password)
            user = self._db.add_user(email=email, hashed_password=hashed_pass)
            return user
        if user:
            raise ValueError("User {} already exists".format(email))
