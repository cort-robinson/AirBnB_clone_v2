#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from operator import attrgetter
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Gets a list of states"""
    states = storage.all('State').values()
    result = sorted(states, key=attrgetter('name'))
    return render_template(
        '8-cities_by_states.html', states=result)


@app.teardown_appcontext
def teardown(self):
    """Quits sqlalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
