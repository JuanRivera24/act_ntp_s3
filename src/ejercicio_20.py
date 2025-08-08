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