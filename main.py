from lib import *

archivo = pedirArchivo()
print(" ")
print("Matriz de adyacencia:")
imprimirMatriz(archivo)
lista = crearDiccDeRelaciones(archivo)
print(" ")
print("Lista de relaciones:")
printListaDeRelaciones(lista)
print(" ")
print("Grafo:")
grafo = crear_grafo_desde_lista(lista)
print(grafo)

path = calcular_ruta(grafo, "B", "H")


print(f'Camino más corto: {path}')
peso_total = obtener_peso_total(grafo, path)
print(f'Peso total del camino: {peso_total}')





