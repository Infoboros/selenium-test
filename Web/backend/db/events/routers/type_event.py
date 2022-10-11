from tortoise.contrib.pydantic import pydantic_model_creator

from db.events.models import TypeEvent

from config import CRUDRouter
from db.events.services.type_event import TypeEventService

router = CRUDRouter(
    pydantic_model_creator(TypeEvent, include=('id', 'description')),
    TypeEvent,
    prefix="/type",
    tags=["Типы событий"]
)


@router.post('/init_types')
async def init_types():
    await TypeEventService.init_types_events()
