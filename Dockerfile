FROM python:3.11.5-slim-bookworm
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  CUSTOM_DEBUG_FLAG=False \
  # Poetry's configuration:
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.8.3

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        libpq-dev \
        build-essential \
        && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.poetry/bin"
ENV USE_POSTGRES=True

WORKDIR /app
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-root --only main --no-interaction
RUN poetry show --tree
COPY . .
RUN rm -rf .venv

# Collect static files for admin pages
RUN python manage.py collectstatic --no-input

EXPOSE 8000
CMD ["poetry", "run", "gunicorn", "--config", "gunicorn_config.py", "sas_backend.wsgi:application"]
