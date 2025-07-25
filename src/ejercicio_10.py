# Mediante un ciclo while, solicita al usuario que escriba palabras. El proceso termina cuando el usuario escriba la palabra \"fin\". Al final, muestra cuántas palabras se leyeron (sin contar \"fin\").

palabras = ""
while palabras != "fin":
    palabras = input("Escribe una palabra: ")
    print(palabras) 