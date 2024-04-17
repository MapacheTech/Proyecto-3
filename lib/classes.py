

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
        return self.printDicc(self.Aristas)
        
    pass
    def printDicc(self,dicc):
        for i in dicc:
            print(f'Vertice: {i}')
            for j in dicc[i]:
                print(F'\tDestino: {j} \n\t\tPeso: {dicc[i][j]}')
        return ''
