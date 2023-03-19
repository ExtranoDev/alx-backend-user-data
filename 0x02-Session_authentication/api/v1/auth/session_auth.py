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
            SessionAuth.user_id_by_session_id[sess_id] = user_id
            return sess_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """retrieves a User ID based on a Session ID"""
        if session_id and type(session_id) is str:
            return SessionAuth.user_id_by_session_id.get(session_id)
        return None
