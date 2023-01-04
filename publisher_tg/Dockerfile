FROM python:3.10.9-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry:
    POETRY_VERSION=1.2.0 \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.local/bin"

WORKDIR publisher_tg/
COPY . .
#RUN pip install pipx && pipx upgrade-all && pipx install "poetry==$POETRY_VERSION" && pipx ensurepath
# RUN poetry install
#RUN poetry install

# RUN apt-get update && apt-get install curl
# RUN curl -sSL https://install.python-poetry.org | python3 - && poetry install
# CMD ["poetry", "run", "python", "publisher_tg/main.py"]

RUN pip install -e .
CMD ["python", "publisher_tg/main.py"]
