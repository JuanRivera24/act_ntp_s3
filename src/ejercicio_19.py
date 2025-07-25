# Con un ciclo for, cuenta cuántas vocales (sin distinción de mayúsculas/minúsculas) hay en la frase frase = \"programacion es divertida\" y muestra el total.

frase = "programacion es divertida"
total = 0
for i in frase:
    if i.isupper():
        total += 1    
print(total)