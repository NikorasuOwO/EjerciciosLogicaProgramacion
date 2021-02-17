
### Ordenar lista sin algoritmos de complejidad cuadrática ###
lista=[3,4,1,-10,10,4]
#print(str(lista))


def Ordenar(lista):
    change = True
    while(change):
        i = 0
        change = False
        while(i < len(lista)-1):
            if(lista[i]>lista[i+1]):
            #    print("[i]" + str(lista[i]) + "[i+1]" + str(lista[i+1]))
                aux = lista[i+1]
                lista[i+1] = lista[i]
                lista[i] = aux
                change = True
            i = i + 1

#Ordenar(lista)
#print(str(lista))

#input("")
