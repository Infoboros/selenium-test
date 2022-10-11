from db.twit.routers.twit import router as twit_router

from fastapi import APIRouter

router = APIRouter()

router.include_router(twit_router)
