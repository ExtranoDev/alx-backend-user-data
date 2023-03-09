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
        if path[-1] == '/':
            path = path[:-1]
        for ex_path in excluded_paths:
            if path in ex_path or ex_path[:-1] in path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Handles authorization header"""
        if request:
            auth_val = request.headers.get('Authorization')
            if auth_val is not None:
                return auth_val
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Authenticates current user"""
        return None
