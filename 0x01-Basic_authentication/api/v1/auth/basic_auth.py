#!/usr/bin/env python3
"""Basic auth"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
import base64


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

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """returns the decoded value of a Base64 string"""
        if type(base64_authorization_header) is not str:
            return None
        try:
            decoded_str = base64.b64decode(base64_authorization_header)
            return decoded_str.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """returns the user email and password
        from the Base64 decoded value"""
        if type(decoded_base64_authorization_header) is not str:
            return (None, None)
        if ':' in decoded_base64_authorization_header:
            return tuple(decoded_base64_authorization_header.split(':'))
        return (None, None)

    def user_object_from_credentials(self, user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if type(user_email) is not str or type(user_pwd) is not str:
            return None
        try:
            user_objects = User.search({"email": user_email})
        except Exception:
            return None
        for user in user_objects:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth
        retrieves the User instance for a request
        """
        if request:
            auth_type = self.authorization_header(request)
        if auth_type:
            auth_val = self.extract_base64_authorization_header(auth_type)
        if auth_val:
            auth_decode = self.decode_base64_authorization_header(auth_val)
        if auth_decode:
            user_cred = self.extract_user_credentials(auth_decode)
        if user_cred:
            email = user_cred[0]
            passwrd = user_cred[1]
            return self.user_object_from_credentials(email, passwrd)
        return None
