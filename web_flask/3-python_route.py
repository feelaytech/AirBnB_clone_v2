#!/usr/bin/python3
"""Starts a Flask application listening on 0.0.0.0:5000."""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns Hello HBNB on route /."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB on route /hbnb."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Returns C <text>. Replace _ with  (space)."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Returns Python <text>. Replace _ with (space)."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
