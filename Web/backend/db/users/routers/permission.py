from typing import List, Optional
from fastapi import APIRouter, Depends, UploadFile
from fastapi.params import File, Form
from pydantic import UUID4

from db.base.services.file_service import FileService
from db.users.schemas import GetUserDetail
from db.users.services.services import permission_service, fastapi_users_service
from db.users.models import User, UserModel
from tortoise.contrib.fastapi import HTTPNotFoundError
from config import MediaPath

permission_router = APIRouter()


@permission_router.get("/", response_model=List[GetUserDetail])
async def get_users(
        limit: Optional[int] = None, offset: Optional[int] = None,
        user: User = Depends(fastapi_users_service.get_current_active_user)
):
    return await permission_service.filter(limit=limit, offset=offset)


@permission_router.get("/me", response_model=GetUserDetail)
async def get_me(user: User = Depends(fastapi_users_service.get_current_active_user)):
    return await permission_service.get(id=user.id)


@permission_router.get("/{user_id}", response_model=GetUserDetail)
async def get_user(
        user_id: str,
        user: User = Depends(fastapi_users_service.get_current_active_user)
):
    return await permission_service.get(id=user_id)


@permission_router.put("/set_avatar/", response_model=GetUserDetail)
async def set_avatar(
        avatar: UploadFile = File(...),
        postfix: str = Form(...),
        user: User = Depends(fastapi_users_service.get_current_active_user)
):
    user = await UserModel.get(id=user.id)

    file_scheme = await FileService.save_file(avatar, MediaPath.user_avatars, postfix)

    user.avatar_id = file_scheme.id
    await user.save()

    return await GetUserDetail.from_tortoise_orm(user)
