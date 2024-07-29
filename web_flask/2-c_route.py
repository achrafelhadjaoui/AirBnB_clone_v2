#!/usr/bin/python3
'''
    A script that starts a Flask web application
'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    '''Display “Hello HBNB!”'''

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''a script that start a flsk app'''

    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    '''display a C followed by the value ot the text variable'''

    return "C {}".format(text)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
