# Utilizando un ciclo while, calcula el factorial de un número entero n introducido por el usuario y muestra el resultado.

n = int(input("Ingrese un número entero: "))
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print(factorial)