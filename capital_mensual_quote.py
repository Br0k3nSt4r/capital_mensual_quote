# Programa para Calcular en cuantos Meses el capital inicial estara duplicado al doble

print("------Programa para calcular--------")
print("El tiempo de duplicacion del capital")

# -----------------
# libraries
# -----------------
import math

# -----------------
# input
# -----------------
c=int(input("Digite su Capital (DINERO) actual: $ "))

# -----------------
# processing
# -----------------
d= 2*c
n= 0

while(c<d):
    c = c+0.05*c
    n = n+1

# -----------------
# output
# -----------------

print("El tiempo en meses aproximado de la duplicacion del Capital (DINERO) es de: "+str(n) + "meses")
print("Su capital duplicado es un total de $"+str(c))