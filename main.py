from lib import *

archivo = "datos-Eval-3.xlsx" #pedirArchivo()
print(" ")
print("Matriz de adyacencia:")
imprimirMatriz(archivo)
lista = crearDiccDeRelaciones(archivo)
print(" ")
print("Lista de relaciones:")
printListaDeRelaciones(lista)
print(" ")
print("Grafo:")
printDicc(lista)

grafoTest = grafo()
for i in lista:
    for j in lista[i]:
      grafoTest.addArista(str(i), str(j), int(lista[i][j]))
      

origenG = 'B'
destinoG = 'H'
visitados = []
path = {}
visitados.append(origenG)
path[origenG] = {'-':0}

llaves = grafoTest.Aristas[origenG].keys()
print(llaves)
print("----------------")
for i in llaves:
    path[i]={origenG : grafoTest.Aristas[origenG][i]}
print("----------------")
print(visitados)
print(path)
print("----------------")

verticeAct = "A"
visitados.append(verticeAct)
llaves = grafoTest.Aristas[verticeAct].keys()
print(llaves)
print("----------------")
for i in llaves:
    if i not in visitados:
        if i not in path: path[i]={}
        llave = list(path[verticeAct].keys())
        acumulado = path[verticeAct][llave[0]]
        path[i].update({verticeAct : grafoTest.Aristas[verticeAct][i]+acumulado})

        if len(path[i]) == 2:
            kiss = list(path[i].keys())
            if kiss[0] > kiss[1]:
                del(path[i][kiss[0]])
            elif kiss[0] < kiss[1]:
                del(path[i][kiss[1]])
            
            pass
print("----------------")
print(path)



print("----------------")
print(path)
verticeAct = "E"
visitados.append(verticeAct)
llaves = grafoTest.Aristas[verticeAct].keys()
print(llaves)
print("----------------")
for i in llaves:
    if i not in visitados:
        if i not in path: path[i]={}
        llave = list(path[verticeAct].keys())
        acumulado = path[verticeAct][llave[0]]
        path[i].update({verticeAct : grafoTest.Aristas[verticeAct][i]+acumulado})

        if len(path[i]) == 2:
            kiss = list(path[i].keys())
            if kiss[0] > kiss[1]:
                del(path[i][kiss[0]])
            elif kiss[0] < kiss[1]:
                del(path[i][kiss[1]])
            
            pass
print("----------------")
print(path)


verticeAct = "H"
visitados.append(verticeAct)
llaves = grafoTest.Aristas[verticeAct].keys()
print(llaves)
print("----------------")
for i in llaves:
    if i not in visitados:
        if i not in path: path[i]={}
        llave = list(path[verticeAct].keys())
        acumulado = path[verticeAct][llave[0]]
        path[i].update({verticeAct : grafoTest.Aristas[verticeAct][i]+acumulado})

        if len(path[i]) == 8:
            kiss = list(path[i].keys())
            for h in range(len(kiss)):
              for k in range(len(kiss)):
                if kiss[h] > kiss[k]:
                  del(path[h][kiss[h]])
                elif kiss[h] < kiss[k]:
                  del(path[h][kiss[k]])
            
                          
            pass
print("----------------")
print(path)


print("B:",path["B"],"A:",path["A"], "E:",path["E"], "H:",path["H"])



