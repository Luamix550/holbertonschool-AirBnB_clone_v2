#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Display "Hello HBNB!" when accessing the root route"""
    return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
    """Display "HBNB" when accessing the /hbnb route"""
    return "HBNB"

@app.route("/c/<text>")
def c_route(text):
    """Display 'C' followed by the value of the text variable"""
    return "C {}".format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
