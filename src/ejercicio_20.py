# Utilizando un ciclo while, solicita al usuario que ingrese edades una a una. El proceso termina cuando se introduzca -1. Al final, muestra la edad mayor que se haya ingresado.

import sys

edades = []
while True:
    edad = int(input("Ingrese una edad: "))
    if edad == -1:
        break
    edades.append(edad)

if edades:
    print("La edad más alta es", max(edades))
else:
    print("No ingresaste ninguna edad")