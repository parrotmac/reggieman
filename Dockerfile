FROM python:3.5
ENV PYTHONUNBUFFERED 1

RUN mkdir /srv/
WORKDIR /srv/
ADD . /srv/

RUN pip install -r requirements.txt

