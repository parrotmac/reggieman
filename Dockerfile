FROM python:3.5
EXPOSE 5000
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /srv/flask
WORKDIR /srv/flask
ADD . /srv/flask/

RUN pip install -r requirements.txt

ENTRYPOINT gunicorn --bind 0.0.0.0:5000 reggieman.wsgi
