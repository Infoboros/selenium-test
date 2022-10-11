from db.events.models import TypeEvent, Event
from db.events.schemas import EventSchema


class EventService:

    @staticmethod
    async def make_event(twit_id: int, type_event: TypeEvent, user_id):
        event, created = await Event.get_or_create(
            twit_id=twit_id,
            type=type_event,
            initiator_id=user_id
        )

        if not created:
            await event.delete()

    @staticmethod
    async def get_feed_for_user(user_id):
        return await EventSchema.from_queryset(Event.filter(twit__author_id=user_id))