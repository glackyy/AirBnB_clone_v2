#!/usr/bin/python3
"""Starting Flask web app"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displaying the main Hbnb filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """Removing the current SqlAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
