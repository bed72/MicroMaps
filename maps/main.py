import settings

from fastapi import FastAPI
from nameko.standalone.rpc import ClusterRpcProxy

app = FastAPI()
CONFIG = {"AMQP_URI": "amqp://user:password@host"}


@app.get("/{arq_name}")
async def read_root(arq_name):
    return get_maps(arq_name)


def get_maps(arq_name):
    date = []
    with ClusterRpcProxy(CONFIG) as rpc:
        date = rpc.maps.get(settings.STATICFILES_DIRS[0] + arq_name + ".osm")

    dict_maps = {i: date[i] for i in range(0, len(date))}
    return dict_maps
