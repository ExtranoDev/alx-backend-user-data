#!/usr/bin/env python3
"""API Authentication"""
from flask import request


class Auth:
    """Class template for all authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """collects authentication path"""
        return False

    def authorization_header(self, request=None) -> str:
        """Handles authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Authenticates current user"""
        return None
