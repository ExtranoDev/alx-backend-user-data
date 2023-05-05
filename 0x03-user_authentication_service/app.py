#!/usr/bin/env python3
"""a basic Flask app"""
from flask import Flask, jsonify, request, abort, make_response
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', strict_slashes=False)
def home():
    """Landing page for app"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """create user"""
    email = request.form['email']
    password = request.form['password']
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Login user and create session ID for them"""
    email = request.form['email']
    password = request.form['password']

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = make_response(jsonify({"email": f"{email}",
                                          "message": "logged in"}))
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logout user"""
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if not user:
            abort(403)
        AUTH.destroy_session(user.id)
        return redirect(url_for('home'))
    abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """Get user profile
    """
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({"email": f"{user.email}"})
    abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """reset password"""
    email = request.form['email']
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": f"{email}",
                        "reset_token": f"{reset_token}"})
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """Update password end-point"""
    email = request.form.get('email')
    new_pass = request.form.get('new_password')
    reset_token = request.form.get('reset_token')
    try:
        AUTH.update_password(reset_token, new_pass)
        return jsonify({"email": f"{email}",
                        "message": "Password updated"})
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
