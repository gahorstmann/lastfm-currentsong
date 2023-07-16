# syntax=docker/dockerfile:1

FROM python:3.11-slim

WORKDIR /app

COPY Pipfile ./

RUN python -m pip install --upgrade pip
RUN pip install pipenv 
RUN pipenv install --dev --deploy

WORKDIR /app
COPY . /app

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD ["python", "main.py"]
EXPOSE 8080