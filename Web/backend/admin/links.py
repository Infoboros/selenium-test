from typing import List

from fastapi_admin.enums import Method
from starlette.requests import Request

from fastapi_admin.app import app
from fastapi_admin.file_upload import FileUpload
from fastapi_admin.resources import Link, Model, Field, Action, ToolbarAction, Dropdown
from fastapi_admin.widgets import displays, filters, inputs

from admin.models import Admin

from config import MediaPath

from db.users.models import UserModel

from db.twit.models import Twit

from db.events.models import TypeEvent, Event

upload = FileUpload(uploads_dir=MediaPath.user_avatars)


@app.register
class Dashboard(Link):
    label = "Дашборд"
    icon = "fas fa-home"
    url = "/admin"


@app.register
class TwitsResource(Model):
    label = "Твиты"
    model = Twit
    icon = "fas fa-envelope"
    page_pre_title = "список твитов"
    page_title = "Twits"

    filters = [
        filters.Search(
            name="text",
            label="Текст",
            search_mode="contains",
            placeholder="Поиск по тексту",
        ),
        filters.Datetime(name="datetime", label="Дата Публикации"),
    ]
    fields = [
        "id",
        "author",
        "text",
        "datetime",
    ]


@app.register
class Events(Dropdown):
    class TypeEventResource(Model):
        label = "Типы событий"
        model = TypeEvent
        icon = "fas fa-book"
        page_pre_title = "Список событий"
        page_title = "TypeEvent"
        filters = [
            filters.Search(
                name="description",
                label="description",
                search_mode="contains",
                placeholder="Поиск по названию",
            )
        ]
        fields = [
            "id",
            "description"
        ]

    class EventResource(Model):
        label = "События"
        model = Event
        icon = "fas fa-calendar"
        page_pre_title = "список событий"
        page_title = "Events"
        filters = [
            filters.Datetime(name="datetime", label="Дата и время события"),
        ]
        fields = [
            "id",
            "twit",
            "initiator",
            "type",
            "datetime"
        ]

    label = "События"
    icon = "fas fa-book"
    resources = [EventResource, TypeEventResource]


@app.register
class Permissions(Dropdown):
    class AdminResource(Model):
        label = "Администраторы"
        model = Admin
        icon = "fas fa-user"
        page_pre_title = "Список пользователей"
        page_title = "Admin"
        filters = [
            filters.Search(
                name="username",
                label="username",
                search_mode="contains",
                placeholder="Поиск администраторов",
            ),
            filters.Date(name="created_at", label="CreatedAt"),
        ]
        fields = [
            "id",
            "username",
            Field(
                name="password",
                label="Password",
                display=displays.InputOnly(),
                input_=inputs.Password(),
            ),
            Field(name="email", label="Email", input_=inputs.Email()),
            Field(
                name="avatar",
                label="Avatar",
                display=displays.Image(width="40"),
                input_=inputs.Image(null=True, upload=upload),
            ),
            "created_at",
        ]

        async def get_toolbar_actions(self, request: Request) -> List[ToolbarAction]:
            return []

        async def cell_attributes(self, request: Request, obj: dict, field: Field) -> dict:
            if field.name == "id":
                return {"class": "bg-danger text-white"}
            return await super().cell_attributes(request, obj, field)

        async def get_actions(self, request: Request) -> List[Action]:
            return []

        async def get_bulk_actions(self, request: Request) -> List[Action]:
            return []

    class UsersResource(Model):
        label = "Пользователи"
        model = UserModel
        icon = "fas fa-users"
        page_pre_title = "список пользователей"
        page_title = "Users"
        filters = [
            filters.Search(
                name="nick_name",
                label="Имя",
                search_mode="contains",
                placeholder="Поиск пользователей",
            ),
            filters.Date(name="date_registration", label="Дата регистрации"),
        ]
        fields = [
            "id",
            "nick_name",
            "id_name",
            "date_registration",
            Field(
                name="hashed_password",
                label="password",
                display=displays.InputOnly(),

                input_=inputs.Password(),
            ),
            Field(name="email", label="Email", input_=inputs.Email()),
        ]

    label = "Управление правами"
    icon = "fas fa-cog"
    resources = [UsersResource, AdminResource]
