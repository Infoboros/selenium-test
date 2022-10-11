from tortoise import models, fields, Tortoise

from config import DBPaths

Tortoise.init_models(DBPaths.base, 'models')


class File(models.Model):
    id = fields.BigIntField(pk=True)
    path = fields.CharField(max_length=250)

    class PydanticMeta:
        include = ('id', 'path')
