num = int(input("Digite un numero"))

lista = []
result = 0

for i in range(1, 11):
  result = i * num
  lista.append(result)

print(lista)