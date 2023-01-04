from config import db_url
from tortoise import Tortoise, run_async
from models_db import Article
import asyncio


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


run_async(create_article("test", "test", "test", "test"))
