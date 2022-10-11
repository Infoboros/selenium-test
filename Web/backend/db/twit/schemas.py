from datetime import datetime
from typing import List

from tortoise.contrib.pydantic import pydantic_model_creator, PydanticModel

from db.events.schemas import EventSchema
from db.twit.models import Twit
from db.users.schemas import GetUserDetail

TwitCreateScheme = pydantic_model_creator(Twit, include=('text',))


class TwitGetScheme(PydanticModel):

    id: int
    author: GetUserDetail
    text: str
    datetime: datetime
    event: List[EventSchema] = []

    class Config:
        orig_model = Twit
        orm_mode = True
