from tortoise import Tortoise, models, fields

from config import DBPaths

Tortoise.init_models(DBPaths.events, 'models')


class TypeEvent(models.Model):
    LIKE = "Лайк"
    REPOST = "Репост"

    id = fields.BigIntField(pk=True)
    description = fields.CharField(max_length=512)

    class PydanticMeta:
        include = ('id', 'description')


class Event(models.Model):
    id = fields.IntField(pk=True)

    twit = fields.ForeignKeyField(
        'models.Twit', related_name='event',
        on_delete=fields.CASCADE, description='Событие'
    )
    initiator = fields.ForeignKeyField(
        'models.UserModel', related_name='event',
        on_delete=fields.CASCADE, description='Инициатор'
    )

    type = fields.ForeignKeyField(
        'models.TypeEvent', related_name='event',
        on_delete=fields.CASCADE, description='Тип события(ретвит, лайк и т.д.)'
    )

    datetime = fields.DatetimeField(auto_now_add=True)

    class Meta:
        ordering = ["-datetime"]