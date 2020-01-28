import xml.etree.cElementTree as et

from nameko.rpc import rpc


class MapsService:
    name = "maps"

    @rpc
    def get(self, arq):
        map = []
        tree = et.parse(arq)
        root = tree.getroot()

        for node in root.iter("node"):
            map.append({"lat": node.attrib["lat"], "lon": node.attrib["lon"]})
        return map
