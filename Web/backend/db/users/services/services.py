from db.users.services.fast_api_users import fastapi_users, cookie_authentication, SECRET
from db.users.services.permission import PermissionService

permission_service = PermissionService()
fastapi_users_service = fastapi_users
