FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt ./

RUN python -m pip install --upgrade pip
RUN  pip install -r requirements.txt

COPY . .

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD ["gunicorn", "main:app"]
EXPOSE 8080