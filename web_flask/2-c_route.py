#!/usr/bin/python3
'''A simple Flask web application.
'''
from flask import Flask


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


if __name__ == '__main__':
    app.run()
