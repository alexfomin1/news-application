from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Article(models.Model):
    id = fields.IntField(pk=True)
    title = fields.TextField()
    summary = fields.TextField(null=True)
    source = fields.CharField(max_length=255)
    url = fields.CharField(max_length=255)
    datetime = fields.DatetimeField(auto_now_add=True)


Article_Pydantic = pydantic_model_creator(Article, name="Article")
