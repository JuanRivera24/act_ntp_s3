n = int(input("Ingrese un número entero positivo: "))
suma = 0
while n > 0:
    suma += n % 10
    n //= 10
print(suma)