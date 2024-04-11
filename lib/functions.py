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

