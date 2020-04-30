FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /web
WORKDIR /web
COPY ./web /web

RUN adduser -D user
USER user
