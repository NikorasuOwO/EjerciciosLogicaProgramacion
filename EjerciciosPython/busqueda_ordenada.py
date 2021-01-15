
### Busqueda lineal en un array ORDENADO unidimensional ###

## SE PRESUPONE QUE LA LISTA ESTÁ ORDENADA ##

from OrdenarListaNlogN import Ordenar
import random

n = 15
lista = []

while(len(lista) <= 10):
    lista.append(random.randint(0,n))

print(str(lista))
Ordenar(lista)
print(str(lista))

numero = 10

def Buscar(numero):
    i = 0
    while(i < len(lista) and lista[i] < numero): #Buscamos número
        i=i+1
    if(i < len(lista) and lista[i] == numero):
        return i
    else:
        return -1

input(str(numero) + "? " + str(Buscar(numero)))
