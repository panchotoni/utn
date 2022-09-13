num = int(input("Ingrese el numero que quiere calcular"))
factorial = 1
while (num < 0):
    print("El numero es negativo")
    num = int(input("Ingrese el numero que quiere calcular"))

for i in range (1, num+1):
    factorial *= i

print(factorial)