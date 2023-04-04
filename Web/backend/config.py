from os import environ, mkdir, listdir
from shutil import rmtree
from fastapi_crudrouter import TortoiseCRUDRouter

DB_URL = environ.get('DB_URL', "sqlite://sql_app.db")
DOMAIN_BACKEND = environ.get('REACT_APP_DOMAIN_BACKEND', "http://localhost:8000")

TMP_DIR = 'TMP_DIR'

if TMP_DIR not in listdir():
    mkdir(TMP_DIR)
else:
    rmtree(TMP_DIR)
    mkdir(TMP_DIR)

CRUDRouter = TortoiseCRUDRouter


class DBPaths:
    users = ['db.users.models']
    base = ['db.base.models']
    twit = ['db.twit.models']
    events = ['db.events.models']
    admin = ['admin.models']

    all_paths = ["aerich.models"] + base + users + twit + events + admin


class MediaPath:
    root = 'static'

    user = 'user'

    user_avatars = f'{root}/{user}/avatars'
    
    sub_dirs = {

        user: [user_avatars],

    }

    @staticmethod
    def init_dirs():
        if MediaPath.root not in listdir():
            mkdir(MediaPath.root)
        for sub_root, sub_paths in MediaPath.sub_dirs.items():
            if sub_root not in listdir(MediaPath.root):
                try:
                    mkdir(f'{MediaPath.root}/{sub_root}')
                except:
                    continue
            for path in sub_paths:
                try:
                    mkdir(path)
                except:
                    continue


TORTOISE_ORM = {
    "connections": {"default": DB_URL},
    "apps": {
        "models": {
            "models": DBPaths.all_paths,
            "default_connection": "default",
        }
    },
}

MediaPath.init_dirs()

SECRET = "PARAVOZIK_TIR_TIR_TIR"
LIFETIME_SESSION = None
