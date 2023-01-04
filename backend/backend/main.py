from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from .models import Article, Article_Pydantic
from .config import db_url, POSTGRES_CONFIG
import backend.models

app = FastAPI(title="4min.News")


@app.get(path="/", name="Новости", response_model=list[Article_Pydantic])
async def index():
    return await Article_Pydantic.from_queryset(
        Article.all().order_by("-datetime").limit(20)
    )


register_tortoise(app, config=POSTGRES_CONFIG)
