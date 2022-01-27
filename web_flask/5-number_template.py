#!/usr/bin/python3
'''A simple Flask web application.
'''
from flask import Flask, render_template


app = Flask(__name__)
'''The Flask application instance.'''


@app.route('/', strict_slashes=False)
def index():
    '''The home page.'''
    return 'Hello HBNB!\n'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''The hbnb page.'''
    return 'HBNB\n'


@app.route('/c/<text>', strict_slashes=False)
def c_page(text):
    '''The c page.'''
    return 'C {}\n'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
def python_page(text):
    '''The python page.'''
    return 'Python {}\n'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_page(n):
    '''The number page.'''
    return '{} is a number\n'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''The number_template page.'''
    ctxt = {
        'n': n
    }
    return render_template('5-number.html', **ctxt)


if __name__ == '__main__':
    app.run()
