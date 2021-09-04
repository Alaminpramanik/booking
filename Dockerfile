
FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app/
ADD . /app/
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt