from pydantic import BaseModel
import datetime


class Article(BaseModel):
    id: int | None
    title: str
    source: str
    link: str
    summary: str | None
    date: datetime.datetime | None


class Article_redis(BaseModel):
    source: str
    link: str
