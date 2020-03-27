FROM python:alpine
LABEL maintainer="Iwork plc" 

ENV env=PYTHONUNBUFFERED

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user


