# Utilizando un ciclo while, simula un reloj digital que muestre cada segundo desde 00:00 hasta 00:59 en formato MM:SS, cada valor en una línea.

import time

while True:
    time.sleep(1)
    print(time.strftime("%M:%S"))