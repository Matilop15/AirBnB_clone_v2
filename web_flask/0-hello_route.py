#!/usr/bin/python3
"""
The application listens on 0.0.0.0, port 5000.
Routes:
    - /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_AirBnB():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
