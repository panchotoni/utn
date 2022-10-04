import random
num = random.randint(0, 100)
numPers = int(input("Digite un numero "))
while(numPers != num):
    if (numPers < num):
        print("El numero es menor")
    else:
        print("El numero es mayor")

    numPers = int(input("Digite otro numero "))

print(f"Felicidades encontraste el numero oculto que es {num}")
