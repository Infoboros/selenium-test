from tortoise import Tortoise, models, fields

from config import DBPaths

Tortoise.init_models(DBPaths.twit, 'models')


class Twit(models.Model):
    id = fields.IntField(pk=True)
    author = fields.ForeignKeyField(
        'models.UserModel', related_name='twit',
        on_delete=fields.CASCADE, description='Автор'
    )
    text = fields.TextField(default="", description='Текст')
    datetime = fields.DatetimeField(auto_now_add=True)

    class Meta:
        ordering = ["-datetime"]
