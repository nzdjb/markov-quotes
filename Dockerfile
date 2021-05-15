FROM python:slim

RUN pip install pipenv

WORKDIR /opt/app

COPY Pipfile* .
RUN pipenv install --system

COPY res res
COPY src src
COPY wsgi.py .

CMD gunicorn --worker-class gevent --bind 0.0.0.0:8080 wsgi:app