#!/usr/bin/env python3
"""a basic Flask app"""
from flask import Flask, jsonify
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
    password = request.form['email']
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 4001


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
