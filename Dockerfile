FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN pip install --upgrade pip && pip install "poetry==2.2.1"

COPY pyproject.toml poetry.lock README.md LICENSE /app/
RUN poetry install --no-interaction --no-ansi

COPY src /app/src
COPY tests /app/tests

CMD ["poetry", "run", "pytest", "tests", "-m", "unit", "-vv"]

