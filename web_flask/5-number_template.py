#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template

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


@app.route('/number/<int:n>')
def is_a_number(n):
    """ Routing with a int as dynamic parameter """
    return '{} is a number'.format(n)@app.route('/number_template/<int:n>')


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Routing with a template as dynamic parameter """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
