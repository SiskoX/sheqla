FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /django
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN apk add build-base

RUN pip install Django==3.2.9
RUN pip install djangorestframework==3.12.4
RUN pip3 install  gunicorn
COPY . .
# 1000 135 987 348