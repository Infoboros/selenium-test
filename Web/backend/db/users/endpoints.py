from fastapi import APIRouter

from db.users.services.services import fastapi_users_service, cookie_authentication, SECRET
from db.users.routers.permission import permission_router

auth_router = fastapi_users_service.get_auth_router(cookie_authentication)
register_router = fastapi_users_service.get_register_router()
reset_password_router = fastapi_users_service.get_reset_password_router(SECRET)

user_router = APIRouter()
user_router.include_router(permission_router, prefix="/permissions")
user_router.include_router(auth_router, prefix="/auth")
user_router.include_router(register_router, prefix="/auth")
user_router.include_router(reset_password_router, prefix="/auth")
