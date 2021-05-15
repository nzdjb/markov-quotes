# Markov Quotes

This is a simple API for creating quotes using Markov chains and an existing list.

To run:

    pipenv install
    gunicorn wsgi:app

Source quotes are read from res/quotes.txt, one per line. This file can be replaced to change the input.

## Credits

res/quotes.txt adapted from https://gist.github.com/erickedji/68802
