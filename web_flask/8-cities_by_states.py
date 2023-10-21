#!/usr/bin/python3
"""Starting Flask web app"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displaying Html Page with a list of all states and related cities"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Removing the current SqlAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
