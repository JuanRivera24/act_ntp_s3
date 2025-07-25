# Mediante un ciclo while, implementa un juego de adivinanza: el programa genera un número aleatorio del 1 al 10 y solicita al usuario que lo adivine. El proceso se repite hasta que el usuario acierte. Muestra un mensaje de felicitación al final.

import random

num = random.randint(1, 10)
while num != int(input("Dime el número: ")):
    num = random.randint(1, 10)
print("Felicitaciones, has adivinado el número!")