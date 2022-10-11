from datetime import datetime, date
from typing import Optional, List

from pydantic import BaseModel, UUID4
from tortoise.contrib.pydantic import PydanticModel

from db.base.schemas import GetFile
from db.users.models import UserModel


class Status(PydanticModel):
    message: str


class UserOrmSchema(PydanticModel):
    class Config:
        orig_model = UserModel
        orm_mode = True


class GetUserDetail(UserOrmSchema):
    id: UUID4

    email: str

    nick_name: str
    id_name: str
    date_registration: Optional[date] = None

    avatar: Optional[GetFile] = None
