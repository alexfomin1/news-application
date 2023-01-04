from tortoise.models import Model
from tortoise import fields


class Article(Model):
    id = fields.IntField(pk=True)
    title = fields.TextField()
    summary = fields.TextField(null=True)
    source = fields.CharField(max_length=255)
    url = fields.CharField(max_length=255)
    datetime = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.title
