#!/usr/bin/env python3
""""Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """expects one string argument name password
    returns a salted, hashed password, which is a byte string"""
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
