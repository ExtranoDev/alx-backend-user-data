#!/usr/bin/env python3
"""a basic Flask app"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Landing page for app"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
