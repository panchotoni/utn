#LISTAS SON LO QUE SE CONOCE COMO ARREGLOS

nombres = ['Naty', 'pancho', 'caro', 'yair']
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(1.2)
print(nombres)

"""#print(nombres[0])
#print(nombres[1])
#print(nombres[3])
#print(nombres[-1])
#print(nombres[-2])

print(nombres[0:2]) #Aca seleccionamos que informacion queremos que se muestre
print(nombres[ :3])
print(nombres[1 : ])

nombres[3] = "Daniela"
print(nombres)

#for nombre in nombres:
#    print(nombre)
#else:
#    print("Se finalizo el ciclo for")
print(len(nombres)) #Tamaño de el array

nombres.append('Marcelo') #Agregamos un valor al final del array
print(nombres)

nombres.insert(1, 'alberto') #Agregamos un valor en un lugar especificado
nombres.insert(3, 'Debora')
print(nombres)

nombres.remove('alberto') #Eliminamos un elemento del array
print(nombres)

nombres.pop() #En este caso borra el ultimo elemento de la lista, y lo podemos guardar en una variable.
print()

del nombres[2] #Eliminamos un elemento especifico
print(nombres)

nombres.clear() #Eliminamos todos los elementos del array
print(nombres)

del nombres #Borramos completamente el array es decir, la variable que lo contenia.
"""
#EJERCICIOSSSSSSSSSSSSS
"""
x = range(3, 10, 2)
for n in x:
    print(n)
print("\n")

y = range(10)
for n in y:
    if n % 3 == 0:
        print(n)
print("\n")

z = range(2, 7) #Hay que tener en cuenta que no toma el ultimo valor del rango seleccionado
for n in z:
    print(n)
"""
#TUPLAS ¡¡¡¡¡¡NO SE PUEDEN MODIFICAR NI NADAAAA XQ SON ESTRICTAS!!!!!!
"""cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

print(cocina[0])

print(cocina[-1])

print(cocina[0:1])

verduras = ('papa', )

for cocinar in cocina: #Recorremos los elementos de la tupla
    print(cocinar, end= " ") #Usamos end= " " para eliminar los saltos de linea

#ACA TRANSFORMAMOS LA TUPLA A LISTA PARA MODIFICARLA, Y DESPUES LA VOLVEMOS A TUPLA
cocinaLista = list(cocina)
cocinaLista[0] = "plato"
cocina = tuple(cocinaLista)
print('\n', cocina)"""

#EJERCICIO TUPLAAAA
'''tupla = (13, 1, 8, 3, 2, 5, 8)
arrayNew = []
for i in tupla:
    if i < 5:
        arrayNew.append(i)
print(arrayNew)'''

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]
lista4 = lista1 + lista2 + lista3 #Concatenamos una lsita
print(lista4)
lista4.extend([10,11,12, 3, 3, 3]) #metodo para agregar valores a una lista
print(lista4)

print(lista4.index(7))#Muestra el indice del elemento que ingreasmo por parametro

print(lista4.count(3))#Muestra la cantidad de veces que se repitio un numero
lista4.reverse()
print(lista4)

#Multiplicar una lista
lista4 = lista4 * 3
print(lista4)

#Metodo de ordenamiento
lista4.sort(reverse=False)
print(lista4)
