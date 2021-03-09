FROM python:3


# Não gerar arquivos pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Não usar stdin/stdout
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
