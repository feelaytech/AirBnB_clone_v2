#!/usr/bin/python3
"""Starts a Flask application listening on 0.0.0.0:5000."""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns Hello HBNB on route /."""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
