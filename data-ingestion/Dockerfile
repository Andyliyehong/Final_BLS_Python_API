FROM python:3.6.8-slim

LABEL Image for a web application

WORKDIR /home

COPY . .

RUN ["pip3", "install", "-r", "requirements.txt"]

ENTRYPOINT ["python", "-m", "app"]
