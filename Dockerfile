FROM python:3.5
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

