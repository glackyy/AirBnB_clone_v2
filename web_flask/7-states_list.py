#!/usr/bin/python3
"""Starting Flask web app"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displaying Html Page with a list of all state obj in dbstorage"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Removing the current SqlAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
