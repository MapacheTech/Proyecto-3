from .functions import *

class grafo():
    def __init__(self) -> None:
        self.Aristas = {}
        pass
    
    def addVertice(self,vertice):
        self.Aristas[vertice] = {}
        pass
    
    def addArista(self, origen, destino,peso):
        if origen not in self.Aristas:
            self.addVertice(origen)
        if destino not in self.Aristas:
            self.addVertice(destino)
        self.Aristas[origen].update({destino:peso})
        pass
    
    def __str__(self) -> str:
        return printDicc(self.Aristas)
        
    pass