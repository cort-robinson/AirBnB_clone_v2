#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from operator import attrgetter
import json
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Gets a list of states"""
    states = storage.all('State').values()
    result = sorted(states, key=attrgetter('name'))
    return render_template(
        '7-states_list.html', states=result)


@app.teardown_appcontext
def teardown(self):
    """Quits sqlalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
