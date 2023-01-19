FROM python:3.10-alpine

RUN apk add --no-cache \
        curl \
        gcc \
        libressl-dev \
        musl-dev \
        libffi-dev \
        bash

RUN pip install poetry
RUN poetry config virtualenvs.create false

WORKDIR app/

COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install --no-root

COPY main.py .
COPY .env .

CMD ["python", "main.py"]
