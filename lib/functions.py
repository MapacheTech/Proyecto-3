import pandas as pd
from .classes import *

def pedirArchivo():
    archivo = input('Cual es el nombre del archivo a procesar? ')
    return archivo
  
def imprimirMatriz(archivo):
  data = pd.read_excel(archivo)
  lista = [data.columns.values.tolist()] + data.values.tolist()
  for fila in lista:
    for elemento in fila:
      if elemento == 'Unnamed: 0':
        elemento = ''  
      elementoStr = str(elemento).ljust(15)  
      print(elementoStr, end=' ')
    print()  
    
def crearDiccDeRelaciones(archivo):
    data = pd.read_excel(archivo)
    lista = [data.columns.values.tolist()] + data.values.tolist()
    dicc = {}
    for fila in lista[1:]:  
        relaciones = {}
        for i, elemento in enumerate(fila[1:], start=1):  
            if elemento != 0:
                relaciones[lista[0][i]] = elemento
        dicc[fila[0]] = relaciones
    return dicc
  
def printListaDeRelaciones(dicc):
  for i in dicc:
    for j in dicc[i]:
      print(F'[{i}]->[{j}]: {dicc[i][j]}', end=' ')
    print()

def crear_grafo_desde_lista(lista,grafo=grafo()):
    for i in lista:
        for j in lista[i]:
            grafo.addArista(str(i), str(j), int(lista[i][j]))
    return grafo

def calcular_ruta(grafo, origenG, destinoG):
  visitados = []
  path = {}
  previo = {}
  visitados.append(origenG)
  path[origenG] = {'-':0}

  llaves = grafo.Aristas[origenG].keys()
  for i in llaves:
    path[i]={origenG : grafo.Aristas[origenG][i]}
    previo[i] = origenG

  verticeAct = "A"
  visitados.append(verticeAct)
  llaves = grafo.Aristas[verticeAct].keys()
  for i in llaves:
    if i not in visitados:
      if i not in path: path[i]={}
      llave = list(path[verticeAct].keys())
      acumulado = path[verticeAct][llave[0]]
      path[i].update({verticeAct : grafo.Aristas[verticeAct][i]+acumulado})
      previo[i] = verticeAct
  

  verticeAct = "E"
  visitados.append(verticeAct)
  llaves = grafo.Aristas[verticeAct].keys()
  for i in llaves:
    if i not in visitados:
      if i not in path: path[i]={}
      llave = list(path[verticeAct].keys())
      acumulado = path[verticeAct][llave[0]]
      path[i].update({verticeAct : grafo.Aristas[verticeAct][i]+acumulado})
      previo[i] = verticeAct
      
  print(f'Path: {path}')


  camino_mas_corto = []
  nodo_actual = destinoG
  while nodo_actual != origenG:
    camino_mas_corto.insert(0, nodo_actual)
    nodo_actual = previo[nodo_actual]
  camino_mas_corto.insert(0, origenG)

  return camino_mas_corto
  
def obtener_peso_total(grafo, camino):
    peso_total = 0
    for i in range(len(camino) - 1):
        peso_total += grafo.Aristas[camino[i]][camino[i+1]]
    return peso_total

