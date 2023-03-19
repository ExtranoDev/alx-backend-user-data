#!/usr/bin/env python3
"""Session definition"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """define session attributes and methods"""
    user_id_by_session_id = dict()

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID and return it"""
        if user_id and type(user_id) is str:
            sess_id = str(uuid.uuid4())
            self.user_id_by_session_id[sess_id] = user_id
            return sess_id
        return None
