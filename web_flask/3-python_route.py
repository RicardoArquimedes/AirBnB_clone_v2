#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, request

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ hello function """
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    """ HBNB function """
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """ Routing with a string as dynamic parameter """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_route(text='is cool'):
    """Python is cool"""
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
