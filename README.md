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
