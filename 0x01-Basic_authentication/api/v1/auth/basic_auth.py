#!/usr/bin/env python3
"""Basic auth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Inherits from Auth class"""
    def extract_base64_authorization_header(self, authorization_header:
                                            str) -> str:
        """returns the Base64 part of the Authorization header
        for a Basic Authentication"""
        if type(authorization_header) is not str:
            return None
        if authorization_header[:6] == 'Basic ':
            return authorization_header[6:]
        else:
            return None
