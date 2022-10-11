from config import DB_URL, DBPaths
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI

from db.users.endpoints import (user_router)
from db.events.endpoints import router as events_router
from db.twit.endpoints import router as twit_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title='Twitter',
    description="API для приложения",
    version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://127.0.0.1:8080'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(user_router, prefix="/users", tags=["Пользователи"])

app.include_router(events_router, prefix="/events", tags=["События"])

app.include_router(twit_router, prefix="/twits", tags=["Твиты"])

app.mount("/static", StaticFiles(directory="static"), name="static")

register_tortoise(
    app,
    db_url=DB_URL,
    modules={"models": DBPaths.all_paths},
    generate_schemas=True,
    add_exception_handlers=True,
)
