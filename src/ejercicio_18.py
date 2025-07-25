# Mediante un ciclo while, genera y muestra la secuencia de Fibonacci empezando por 1, 1, 2, 3, 5, … y termina cuando se alcance el primer valor mayor que 1000.

numero = 1
while numero < 1001:
    print(numero)
    numero, anterior = anterior, numero + anterior