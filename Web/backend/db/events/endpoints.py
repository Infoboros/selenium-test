from fastapi import APIRouter

from db.events.routers.event import router as event_router
from db.events.routers.type_event import router as type_event_router

router = APIRouter()
router.include_router(type_event_router)
router.include_router(event_router, prefix="/events")

