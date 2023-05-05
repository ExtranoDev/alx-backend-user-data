#!/usr/bin/env python3
"""
Hash User password
"""
import bcrypt

def _hash_password(password: str) -> bytes:
    """Helps hash a password
    """
    password = password.encode('utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())

