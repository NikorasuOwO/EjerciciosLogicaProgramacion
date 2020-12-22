
### ALGORITMO DE EUCLIDES ###

print("\n### ALGORITMO DE EUCLIDES ###\n")
print("Dime dos números: ")

a = int(input(""));
b = int(input(""));

A = a
B = b

if(not(a > b)):
    print("Has introducido dos números inadecuados para el algoritmo de euclides")
    input()
    exit()

resto = -1
listaCocientes = []
index = 0
cociente = 0

while(resto != 0):
    restoAnterior = resto
    resto = a%b
    cociente = a//b
    listaCocientes.append(cociente)
    a = b
    b = resto
    index = index + 1

print("El máximo común divisor de "+str(A) + " y " + str(B) + " es "+str(restoAnterior))

print(str(A) + "/" + str(B) + " se puede escribir: q = " + str(listaCocientes))

input()
