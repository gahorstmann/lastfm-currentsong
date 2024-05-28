# Usar a imagem oficial do Python 3.11
FROM python:3.11-slim

# Exponha a porta que o Gunicorn usará
EXPOSE 8080

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instalar dependências necessárias para pipenv e compilar pacotes Python
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar Pipenv
RUN pip install --no-cache-dir pipenv

# Copiar arquivos Pipfile e Pipfile.lock para o diretório de trabalho
COPY Pipfile Pipfile.lock ./

# Instalar dependências do projeto
RUN pipenv install --deploy --system

# Copiar o restante do código da aplicação
COPY . .

# Comando para rodar a aplicação
CMD ["python", "main.py"]
