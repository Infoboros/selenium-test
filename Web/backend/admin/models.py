from datetime import datetime

from tortoise import fields, Model

from fastapi_admin.models import AbstractAdmin

from admin.enums import Status


class Admin(AbstractAdmin):
    last_login = fields.DatetimeField(description="Last Login", default=datetime.now)
    email = fields.CharField(max_length=200, default="")
    intro = fields.TextField(default="")
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}#{self.username}"

class Config(Model):
    label = fields.CharField(max_length=200)
    key = fields.CharField(max_length=20, unique=True, description="Unique key for config")
    value = fields.JSONField()
    status: Status = fields.IntEnumField(Status, default=Status.on)
