import sys
from tortoise import Tortoise
from loguru import logger
from models_db import Article
from config import db_url

logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")


async def create_article(
    title,
    summary,
    source,
    url,
):
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["models_db"]},
    )

    await Tortoise.generate_schemas()

    await Article.create(title=title, summary=summary, source=source, url=url)

    await Tortoise.close_connections()


async def get_latest_article_by_source(source):
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["models_db"]},
    )

    await Tortoise.generate_schemas()

    article = await Article.filter(source=source).order_by("-datetime").first()

    await Tortoise.close_connections()

    return article


async def get_n_latest_articles(n):
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["models_db"]},
    )

    await Tortoise.generate_schemas()

    list_of_articles = await Article.order_by("-datetime").limit(n)

    await Tortoise.close_connections()

    return list_of_articles


async def exists_source(source):
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["models_db"]},
    )

    await Tortoise.generate_schemas()

    result = await Article.filter(source=source).exists()

    await Tortoise.close_connections()

    return result


async def get_latest_article_url_by_source(source):
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["models_db"]},
    )

    await Tortoise.generate_schemas()

    article = await Article.filter(source=source).order_by("-datetime").first()

    await Tortoise.close_connections()

    return article.url
