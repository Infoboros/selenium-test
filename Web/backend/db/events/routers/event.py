from typing import List

from fastapi import APIRouter
from fastapi.params import Depends

from db.events.models import TypeEvent
from db.events.schemas import MakeEventSchema, EventSchema
from db.events.services.event import EventService
from db.users.models import User
from db.users.services.services import fastapi_users_service

router = APIRouter()


@router.put("/like")
async def like(
        schema: MakeEventSchema,
        user: User = Depends(fastapi_users_service.get_current_active_user)
):
    await EventService.make_event(schema.twit_id,
                                  await TypeEvent.get(description=TypeEvent.LIKE),
                                  user.id)


@router.put("/repost")
async def like(
        schema: MakeEventSchema,
        user: User = Depends(fastapi_users_service.get_current_active_user)
):
    await EventService.make_event(schema.twit_id,
                                  await TypeEvent.get(description=TypeEvent.REPOST),
                                  user.id)


@router.get("/feed", response_model=List[EventSchema])
async def feed(user: User = Depends(fastapi_users_service.get_current_active_user)):
    return await EventService.get_feed_for_user(user.id)
