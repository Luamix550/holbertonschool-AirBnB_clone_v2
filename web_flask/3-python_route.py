#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Display "Hello HBNB!" when accessing the root route"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Display "HBNB" when accessing the /hbnb route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Display 'C' followed by the value of the text variable"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', default={"text": "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Display "Python " when accessing the /python/<text> route """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
