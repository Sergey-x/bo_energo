ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim

RUN apt-get update && pip install poetry && poetry config virtualenvs.create false

WORKDIR /bo_energo

COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install --no-cache -r ./requirements.txt

COPY . .


ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 8088 --reload
