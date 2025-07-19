# Utilizando un ciclo while, solicita al usuario que ingrese números. El proceso termina cuando el usuario escriba 0. Al final, muestra la suma total de todos los números ingresados.

suma = 0
while True:
    n = int(input("Ingrese un número: "))
    if n == 0:
        break
    suma += n
print(suma)