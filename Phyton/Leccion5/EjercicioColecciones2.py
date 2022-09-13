#Cree dos listas
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera y no en la segunda
# 3 Lista de palabras que aparecen en la segunda y no en la primera
# 4 Lista de palabras que aparecen en ambas
list1 = [1,2,3,4,5,4,3,2,2,1]
list2 = [4,5,6,7,8,3,1,3,4,5]

list1set = set(list1)
list2set = set(list2)

union = list(list1set | list2set) #Unimos los dos set y los transformamos en lista

solo1 = list(list1set - list2set) #Mostramos solo los elemento que aparecen en la primer lista

solo2 = list(list2set - list1set)

iguales = list(list1set & list2set)

print(f"Lista de palabras que aparecen en las listas {union}")
print(f"Lista de palabras que aparecen en la primera y no en la segunda {solo1}")
print(f"Lista de palabras que aparecen en la segunda y no en la primera {solo2}")
print(f"Lista de palabras que aparecen en ambas {iguales}")


