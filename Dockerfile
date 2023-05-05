FROM python:3.11

WORKDIR /weather-app

COPY . .

RUN pip install requests

ENTRYPOINT ["python", "weather1.py"]

CMD ["Prague", "Paris", "Milan"]