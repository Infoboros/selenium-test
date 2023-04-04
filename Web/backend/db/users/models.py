from datetime import date

from fastapi_users.db import TortoiseBaseUserModel, TortoiseUserDatabase
from fastapi_users import models
from tortoise import fields, Tortoise
from typing import Optional

from tortoise.contrib.pydantic import PydanticModel

from config import DBPaths
from db.base.models import File


class UserModel(TortoiseBaseUserModel):
    nick_name = fields.CharField(max_length=150, default="", description="никнейм")
    id_name = fields.CharField(max_length=150, default="", description="id никнейм")

    date_registration = fields.DatetimeField(auto_now_add=True, description='Дата регистрации')

    avatar = fields.ForeignKeyField(
        'models.File', related_name='user', on_delete=fields.SET_NULL,
        null=True, default=None, description='Аватар'
    )

    class PydanticMeta:
        include = ('id', 'nick_name', 'id_name', 'date_registration', 'avatar')

    def __str__(self):
        return self.email


Tortoise.init_models(DBPaths.users, 'models')


class User(models.BaseUser):
    nick_name: str
    id_name: str

    is_staff: Optional[bool] = False

    class Config:
        orm_mode = True
        orig_model = UserModel


class UserCreate(models.BaseUserCreate):
    nick_name: str
    id_name: str

    class Config:
        orm_mode = True
        orig_model = UserModel


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB, PydanticModel):
    pass


user_db = TortoiseUserDatabase(UserDB, UserModel)
