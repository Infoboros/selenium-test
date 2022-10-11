from pydantic import BaseModel
from tortoise.contrib.pydantic import PydanticModel, pydantic_model_creator
from db.base.models import File
from config import DOMAIN_BACKEND


class Status(BaseModel):
    message: str


class GetFile(PydanticModel):
    id: int
    url: str = None
    path: str

    def __init__(self, **kwargs):
        super(GetFile, self).__init__(**kwargs)
        self.url = f'{DOMAIN_BACKEND}/{self.path}'

    class Config:
        orig_model = File


class URL(PydanticModel):
    url: str
