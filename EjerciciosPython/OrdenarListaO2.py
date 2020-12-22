
### Ordenar lista, complejidad O2 ###

lista = [2,3,5,8,3,9,0,4]
listaOrdenada = []

print(str(lista))

index = 0

def minLista(lista):

    min = lista[0];
    index = 0
    for i in lista:
        if(min > i):
            min = i
            index = index + 1
    return min

for i in range(1,len(lista)):
    min = minLista(lista)
    listaOrdenada.append(min)
    lista.remove(min)

print(str(listaOrdenada))
input("")
