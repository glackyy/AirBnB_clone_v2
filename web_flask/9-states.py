#!/usr/bin/python3
"""Starting Flask web app"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displaying Html Page with a list of all states"""
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displaying Html page with info about <id>, if it exists"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Removing the current SqlAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
