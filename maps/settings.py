import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Database
DATABASES = {
    "host": "localhost",
    "port": "5432",
    "user": "postgres",
    "pasword": "cicada3301",
}


STATICFILES_DIRS = [
    os.path.join(os.path.normpath(BASE_DIR), "maps\\files\\"),
]

