#!/usr/bin/env python3
""""Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """expects one string argument name password
    returns a salted, hashed password, which is a byte string"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_pass: bytes, password: str) -> bool:
    """Function that 2 arguments and returns a boolean.
    args:
        hashed_password: bytes type
        password: string type
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_pass)
