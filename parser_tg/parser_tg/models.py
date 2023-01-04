import sys

from loguru import logger
from pydantic import BaseModel, ValidationError

logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")


class Article(BaseModel):
    title: str
    content: str
    chat_id: str
    article_id: str
    source: str


def validate_article(title, content, chat_id, article_id, source):
    try:
        article = Article(
            title=title,
            content=content,
            chat_id=chat_id,
            article_id=article_id,
            source=source,
        )
        return article
    except ValidationError:
        logger.error("Article validation failed")
        return False
