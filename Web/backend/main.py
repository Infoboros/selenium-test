import os

import redis.asyncio as redis
from fastapi_admin.app import app as admin_app
from fastapi_admin.exceptions import unauthorized_error_exception, forbidden_error_exception, not_found_error_exception, \
    server_error_exception
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN, \
    HTTP_401_UNAUTHORIZED

from admin.models import Admin
from admin.routes import *
from admin.links import *
from admin.providers import LoginProvider
from config import DB_URL, DBPaths
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI

from db.users.endpoints import (user_router)
from db.events.endpoints import router as events_router
from db.twit.endpoints import router as twit_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

login_provider = LoginProvider(
                    login_logo_url="https://preview.tabler.io/static/logo.svg",
                    admin_model=Admin,
                )

app = FastAPI(
    title='Twitter',
    description="API для приложения",
    version="0.0.1",
    root_path='/api'
)

app.mount("/admin", admin_app)
admin_app.add_exception_handler(HTTP_500_INTERNAL_SERVER_ERROR, server_error_exception)
admin_app.add_exception_handler(HTTP_404_NOT_FOUND, not_found_error_exception)
admin_app.add_exception_handler(HTTP_403_FORBIDDEN, forbidden_error_exception)
admin_app.add_exception_handler(HTTP_401_UNAUTHORIZED, unauthorized_error_exception)

@app.on_event("startup")
async def startup():
    r = redis.from_url(
        "redis://cache:6379",
        decode_responses=True,
        encoding="utf8",
    )
    await admin_app.configure(
        logo_url="https://preview.tabler.io/static/logo-white.svg",
        template_folders=[os.path.join(os.path.dirname(os.path.abspath(__file__)), 'admin', "templates")],
        providers=[login_provider],
        redis=r,
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://127.0.0.1:8080'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    expose_headers=["*"],
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
