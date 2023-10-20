#!/usr/bin/python3
"""Starts a Flask application listening on 0.0.0.0:5000."""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """Returns a HTML page with the list of all State objects and
       their corresponding cities present in DBStorage sorted by name.
    """
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Removes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
