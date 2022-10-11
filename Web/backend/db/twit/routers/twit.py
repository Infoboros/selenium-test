from typing import List

from fastapi import APIRouter
from fastapi.params import Depends

from db.events.models import Event
from db.twit.models import Twit
from db.twit.schemas import TwitGetScheme, TwitCreateScheme
from db.users.models import User
from db.users.services.services import fastapi_users_service

router = APIRouter()


@router.post('/', response_model=TwitGetScheme)
async def create(
        schema: TwitCreateScheme,
        user: User = Depends(fastapi_users_service.get_current_active_user)
):
    twit = await Twit.create(
        text=schema.text,
        author_id=user.id
    )

    return await TwitGetScheme.from_tortoise_orm(twit)


@router.get('/feed', response_model=List[TwitGetScheme])
async def get_feed():
    return await TwitGetScheme.from_queryset(
        Twit.all()
    )


@router.get('/profile_feed', response_model=List[TwitGetScheme])
async def get_profile_feed(user: User = Depends(fastapi_users_service.get_current_active_user)):
    repost_events = await Event.filter(initiator_id=user.id)
    reposted_twit_ids = [repost_event.twit_id for repost_event in repost_events]

    my_twits_ids = [twit.id for twit in await Twit.filter(author_id=user.id)]

    feed_ids = my_twits_ids + [
        repost_id for repost_id in reposted_twit_ids
        if repost_id not in my_twits_ids
    ]

    return await TwitGetScheme.from_queryset(
        Twit.filter(id__in=feed_ids)
    )
