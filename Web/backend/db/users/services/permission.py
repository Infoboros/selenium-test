from typing import Optional

from config import MediaPath
from db.base.services.base_service import BaseService
from db.users.models import UserModel
from db.users.schemas import GetUserDetail


class PermissionService(BaseService):
    model = UserModel
    get_schema = GetUserDetail
    get_detail = GetUserDetail

    async def get(self, **kwargs) -> GetUserDetail:
        user: UserModel = await self.model.get(**kwargs)
        return await GetUserDetail.from_tortoise_orm(user)
