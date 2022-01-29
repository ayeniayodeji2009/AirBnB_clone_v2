#!/usr/bin/python3
'''A simple Flask web application.
'''
from flask import Flask, render_template

from models import storage
from models.state import State


app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<state_id>')
def states(state_id=None):
    '''The states page.'''
    states = None
    state = None
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)
    for state in all_states:
        state.cities.sort(key=lambda x: x.name)
    if state_id is not None:
        res = list(filter(lambda x: x.id == state_id, all_states))
        if len(res) > 0:
            state = res[0]
    else:
        states = all_states
    ctxt = {
        'states': states,
        'state': state
    }
    return render_template('9-states.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    '''The Flask app/request context end event listener.'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
