FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt ./

RUN python -m pip install --upgrade pip
RUN  pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
EXPOSE 8080