import random

num = random.randint(1, 10)
while num != int(input("Dime el número: ")):
    num = random.randint(1, 10)
print("Felicitaciones, has adivinado el número!")