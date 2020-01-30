import settings

from fastapi import FastAPI
from nameko.standalone.rpc import ClusterRpcProxy

app = FastAPI()
config: str = {"AMQP_URI": "amqp://bed:cicada3301@192.168.1.166"}


@app.get("/{arq_name}")
async def root(arq_name: str) -> list:
    """Rota implementa seguintes funções
    :param (arq_name) nome da região que deseja obter os dados
    :return list com dados de 'lon' e 'lat' da região informada
    """
    date: list = []
    osm: str = f"{settings.STATICFILES_DIRS[0]}{arq_name}.osm"
    try:
        with ClusterRpcProxy(config) as rpc:
            with open(osm) as arq:
                """ EAFP E melhor pedir perdão do que permissão, 'para arquivo's """
                # Passando tarefa de extrair os dados para o MicroServiço
                date = rpc.maps.get(osm)
                # Se tudo der certo retorna um JSON dos dados lon, lat!
                return date
    except FileNotFoundError:
        # Tratando erro caso o arquivo não exista
        return {"Opps!": "Esse arquivo não existe! :()"}
