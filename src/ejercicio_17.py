# Con un ciclo for, solicita al usuario que ingrese un número entero positivo y calcula la suma de sus dígitos, mostrando el resultado final.

n = int(input("Ingrese un número entero positivo: "))
suma = 0
while n > 0:
    suma += n % 10
    n //= 10
print(suma)