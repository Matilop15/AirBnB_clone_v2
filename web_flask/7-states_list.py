#!/usr/bin/python3
"""
/states_list: Display a HTML page:
H1 tag: “States”
UL tag: with the list of all State objects present
in DBStorage sorted by name (A->Z)
LI tag: description of one State: <state.id>: <B><state.name></B>
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    
    """
    new_states = storage.all(State).values()
    return render_template("7-states_list.html", final_states=new_states)


@app.teardown_appcontext
def teardown_close(exceptions):
    """
    method teardown
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)