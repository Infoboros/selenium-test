from datetime import datetime

from pydantic import BaseModel
from tortoise.contrib.pydantic import PydanticModel, pydantic_model_creator

from db.events.models import Event, TypeEvent
from db.users.schemas import GetUserDetail

TypeEventSchema = pydantic_model_creator(TypeEvent, include=('id', 'description'))


class MakeEventSchema(BaseModel):
    twit_id: int


class EventSchema(PydanticModel):
    id: int

    initiator: GetUserDetail
    type: TypeEventSchema

    datetime: datetime

    class Config:
        orig_model = Event
