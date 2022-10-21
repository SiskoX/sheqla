FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
RUN pip3 install  gunicorn
RUN pip3 install pillow

COPY . .
# 1000 135 987 348