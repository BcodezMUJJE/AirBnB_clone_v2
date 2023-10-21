#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Route that displays a list of states.
    """
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_storage(exception):
    """
    Closes the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
