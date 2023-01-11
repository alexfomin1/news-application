# News aggregation service

## Services used in the project
- Python 3.10.9
    - FastAPI
    - Telethon
    - Aiohttp
    - Toroise-ORM
    - aioredis
    - aio-pika
- Redis (for cache)
- RabbitMQ
- PostgreSQL

## Installation
1. `git clone https://github.com/alexfomin1/news-application.git`
2. `cd news-application`
3. Add `config.py` files to microservices' directories
4. `docker-compose up -d --build`
3. Use `docker-compose stop` to stop the project

## Structure
- parser_rss -- Parsing RSS news
- publisher_tg -- Publishing in telegram channel
- parser_tg -- Parsing in Telegram (in development)
- backend -- API

.
├── README.md
├── backend
│   ├── Dockerfile
│   ├── README.md
│   ├── backend
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── main.py
│   │   └── models.py
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── tests
│       └── __init__.py
├── docker-compose.yml
├── parser_rss
│   ├── Dockerfile
│   ├── README.md
│   ├── migrations
│   ├── parser_rss
│   │   ├── __init__.py
│   │   ├── actions_db.py
│   │   ├── config.py
│   │   ├── full_check.py
│   │   ├── headers.py
│   │   ├── links.py
│   │   ├── main.py
│   │   ├── messaging.py
│   │   ├── models.py
│   │   ├── models_db.py
│   │   ├── parser.py
│   │   ├── redising.py
│   │   └── test.py
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── tests
│       └── __init__.py
├── parser_tg
│   ├── README.md
│   ├── parser_tg
│   │   ├── __init__.py
│   │   ├── actions_db.py
│   │   ├── chat_processing.py
│   │   ├── config.py
│   │   ├── full_check.py
│   │   ├── headers.py
│   │   ├── links.py
│   │   ├── list_of_chats.py
│   │   ├── main.py
│   │   ├── messaging.py
│   │   ├── models.py
│   │   ├── models_db.py
│   │   ├── parser.py
│   │   └── redising.py
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── tests
│       └── __init__.py
├── poetry.lock
├── publisher_tg
│   ├── Dockerfile
│   ├── README.md
│   ├── poetry.lock
│   ├── publisher_tg
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── formatting.py
│   │   ├── main.py
│   │   └── publishing.py
│   ├── pyproject.toml
│   └── tests
│       └── __init__.py
└── pyproject.toml
