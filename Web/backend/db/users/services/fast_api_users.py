from fastapi_users.authentication import CookieAuthentication
from fastapi_users import FastAPIUsers

from config import SECRET, LIFETIME_SESSION

from db.users.models import *

cookie_authentication = CookieAuthentication(
    secret=SECRET,
    lifetime_seconds=LIFETIME_SESSION,
    cookie_secure=False
)

fastapi_users = FastAPIUsers(
    user_db,
    [cookie_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)
