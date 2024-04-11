import pandas as pd

def pedirArchivo():
    archivo = input('Cual es el nombre del archivo a procesar? ')
    return archivo
  
def imprimirMatriz(archivo):
  data = pd.read_excel(archivo)
  lista = [data.columns.values.tolist()] + data.values.tolist()
  for fila in lista:
    for elemento in fila:
      if elemento == 'Unnamed: 0':
        elemento = ''  # Reemplazamos 'Unnamed: 0' con un espacio vacío
      elementoStr = str(elemento).ljust(15)  
      print(elementoStr, end=' ')
    print()  
    
def crearDiccDeRelaciones(archivo):
    data = pd.read_excel(archivo)
    lista = [data.columns.values.tolist()] + data.values.tolist()
    dicc = {}
    for fila in lista[1:]:  # Ignoramos la fila de encabezados
        relaciones = {}
        for i, elemento in enumerate(fila[1:], start=1):  # Ignoramos el primer elemento de la fila
            if elemento != 0:
                relaciones[lista[0][i]] = elemento
        dicc[fila[0]] = relaciones
    return dicc
  
def printListaDeRelaciones(dicc):
  for i in dicc:
    for j in dicc[i]:
      print(F'[{i}]->[{j}]: {dicc[i][j]}', end=' ')
    print()

def printDicc(dicc):
    for i in dicc:
        print(f'Vertice: {i}')
        for j in dicc[i]:
            print(F'\tDestino: {j} \n\t\tPeso: {dicc[i][j]}')
    return ''

def dijkstra(grafo, inicio):
  distancias = {vertice: float('infinity') for vertice in grafo}
  distancias[inicio] = 0

  vertices_no_visitados = list(grafo.keys())

  while vertices_no_visitados:
    vertice_actual = min(
      [(distancias[vertice], vertice) for vertice in vertices_no_visitados], key=lambda x: x[0]
    )[1]

    if distancias[vertice_actual] == float('infinity'):
      break

    for vecino, peso in grafo[vertice_actual].items():
      distancia_alternativa = distancias[vertice_actual] + peso
      if distancia_alternativa < distancias[vecino]:
        distancias[vecino] = distancia_alternativa

    vertices_no_visitados.remove(vertice_actual)

  return distancias

# Usar la función dijkstra para obtener las distancias más cortas desde el vértice de inicio


# Eliminar los elementos que no sean del camino más corto
