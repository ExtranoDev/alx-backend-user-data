#!/usr/bin/env python3
"""
New view for Session Authentication mandatory
"""

from flask import request, abort, jsonify
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', method=['POST'], strict_slashes=False)
def view_session_auth():
    """Authentication Session View"""
    email = request.form.get('email', None)
    password = request.form.get('password', None)

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

        try:
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            session_name = os.getenv('SESSION_NAME')
            response.set_cookie(session_name, session_id)
            return response
        except Exception:
            return jsonify({"error": "no user found for this email"}), 404
