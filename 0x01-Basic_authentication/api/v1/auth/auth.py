#!/usr/bin/env python3
"""API Authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class template for all authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """collects authentication path"""
        if path is None or excluded_paths in (None, []):
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Handles authorization header"""
        auth_val = request.headers.get('Authorization')
        if auth_val is not None:
            return auth_val
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Authenticates current user"""
        return None
