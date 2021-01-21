#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from operator import attrgetter
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>')
def states_by_id(id=None):
    """Gets a list of states"""
    states = storage.all('State').values()
    if (id is None):
        result = sorted(states, key=attrgetter('name'))
        return render_template(
            '9-states.html', states=result)
    for state in states:
        if state.id == id:
            return render_template(
                '9-states.html', states=state, id=id)
    return render_template('9-states.html', states=None, id=id)


@app.teardown_appcontext
def teardown(self):
    """Quits sqlalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
