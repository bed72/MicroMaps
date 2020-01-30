import xml.etree.cElementTree as et

from nameko.rpc import rpc


class MapsService:
    # Nome do Microserviço
    name: str = "maps"

    @rpc
    def get(self, arq: str) -> list:
        """Microserviço implementa seguintes funções
        :param (arq) nome da região que deseja obter os dados, vindo pela 'url'
        :return list com dados de 'lon' e 'lat' da região informada
        """
        try:
            map: list = []
            """ Configurações da lib 'xml.etree.cElementTree' """
            # Passando nome completo do arquivo para variavel 'tree'
            tree = et.parse(arq)
            root = tree.getroot()
            """ Passando tarefas para lib cElementTree para extrair dados do arquivo
                a mesma percore cada 'nodo' da estrutura do arquivo .osm e pega os 
                valores de 'lon' e 'lat', adiciona um 'dict' na lista e retorna 
                para a rota dar um 'response' -> resposta.
            """
            for node in root.iter("node"):
                map.append({
                    "lat": node.attrib["lat"],
                    "lon": node.attrib["lon"]
                })
            return map
        except Exception as identifier:
            # Tratando Exception de forma generica
            return str({'Error': str(identifier)})
