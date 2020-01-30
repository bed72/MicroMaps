import os

# Para indetificar a raiz do modulo python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
""" Futura conexão com DATABASE """
DATABASES: dict = {
    "host": "localhost",
    "port": "5432",
    "user": "postgres",
    "pasword": "cicada3301",
}

# Lista que indentifa os arquivos .osm
STATICFILES_DIRS: list = [
    os.path.join(os.path.normpath(BASE_DIR), "maps\\files\\"),
]
