FROM python:3-slim

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./
RUN pip install pipenv
RUN pipenv install

RUN mkdir spotipyql
COPY spotipyql ./spotipyql

ENV FLASK_APP spotipyql
ENV FLASK_ENV production

RUN ls -l
CMD [ "pipenv", "run", "flask", "run", "-h", "0.0.0.0"]