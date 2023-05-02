FROM python:3.9-slim

WORKDIR /weather-app

COPY . .

RUN pip install requests

CMD python weather1.py