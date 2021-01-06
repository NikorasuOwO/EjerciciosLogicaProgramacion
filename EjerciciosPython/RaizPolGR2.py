### Calcular raices de un npolinomio de grado 2 ###

import math

a = int(input("Coeficiente de x^2: "))
b = int(input("Coeficiente de x: "))
c = int(input("Coeficiente independiente: "))

print("\n\n")

def delta(a,b,c):
    return b*b - 4*a*c

delta = delta(a,b,c)

if(delta == 0):
    print("Hay raíz doble y es: " + str(-b/2*a))

if(delta < 0):

    print("No hay soluciones reales, las soluciones complejas son: ")

    print("\n x1 = "+str(b/(2*a)) + "+" + str(math.sqrt(-delta)/(2*a)) + "i" )

    print("\n x2 = "+str(b/(2*a)) + "-" + str(math.sqrt(-delta)/(2*a)) + "i" )

if(delta > 0):

    x1 =  - b + math.sqrt(delta)
    x1 = x1/(2*a)

    x2 =  - b - math.sqrt(delta)
    x2 = x2/(2*a)

    print("x1: " + str(x1) + " | x2: " + str(x2) )

input()
