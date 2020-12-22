
### Ordenar lista sin algoritmos de complejidad cuadrática ###
lista=[3,4,1,0,10,4]
aux = 0

def Swap0(lista):
    i = 0
    while(i < len(lista)-1):
        change = False
        if(lista[i]>lista[i+1]):
            aux = lista[i+1]
            lista[i+1] = lista[i]
            lista[i] = aux
            change = True
        i = i + 1
        print("i: " + str(lista))
    return change


while(Swap0(lista)):
    print(str(lista)+"...")

print("FINAL:"+str(lista))

input("")
