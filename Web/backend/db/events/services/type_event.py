from db.events.models import TypeEvent


class TypeEventService:

    @staticmethod
    async def init_types_events():
        for description in [TypeEvent.REPOST, TypeEvent.LIKE]:
            await TypeEvent.get_or_create(description=description)
