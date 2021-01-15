
### Busqueda lineal en un array unidimensional ###

import random

n = 10
lista = []
numero = 10

while(len(lista) < 10):
    lista.append(random.randint(0,n))

#print(str(lista))

def Buscar(numero):
    i = 0
    while i < len(lista) and lista[i] != numero:
        i = i + 1

    if(i < len(lista):
        return i
    else:
        return -1
#input("10? " + str(Buscar(numero)))
