# Con un ciclo for, cuenta cuántas letras “a” (minúscula) hay en la cadena texto = "manzana" y muestra el total.

texto = "manzana"
letras = 0
for letra in texto:
    if letra == "a":
        letras += 1
print(letras)   