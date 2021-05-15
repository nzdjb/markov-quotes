"""Markov quotes"""

from os import path
from flask import Flask
import markovify

def create_app():
    """Setup the app"""
    app = Flask(__name__)
    quotes_path = path.join(path.dirname(__file__), '..', 'res', 'quotes.txt')
    with open(quotes_path) as quotes_file:
        model = markovify.NewlineText(quotes_file.read())

    @app.route('/')
    #pylint: disable=unused-variable
    def quote():
        return model.make_sentence()

    return app
