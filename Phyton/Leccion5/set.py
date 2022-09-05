#SETTTTTTTTTT
#Son como listas pero no tienen un orden
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)
print(len(planetas))#Usamos el metodo length
print("Marte" in planetas)#Aca verificamos si existe tal elemento
print("Marte" not in planetas)

planetas.add("Tierra")#Agregamos un elemento
print(planetas)

planetas.remove("Jupiter")#Eliminamos un elemento pero si no esta tira error
print(planetas)

planetas.discard("Tiera")#Con este metodo si no esta el elemento que buscamos no se borra, pero no tira error.
print(planetas)

planetas.clear()#Aca eliminamos todos los elementos del set
print(planetas)

del planetas #Aca eliminamos diractamente set

#********************REPASOOOOO SET O CONJUNTO (LISTAS DESORDENADAS)*************************

conjunto = set()
conjunto1 = {"bye", }
conjunto.add(7)
conjunto.add('hola')
print(conjunto)
conjunto1.add("hola")
print(conjunto1)

print(3 not in conjunto) #PREGUNTAMOS SI ESTTA ESE VALOR EN EL SET

print(conjunto == conjunto1)#Preguntamos si son iguales

#OPERACIONES DE CONJUNTOS
conjunto3 = conjunto | conjunto1 #UNIMOS LOS DOS CONJUNTOS
print(conjunto3)

conjunto3 = conjunto & conjunto1 #QUE ELEMENTO TIENE EN COMUN
print(conjunto3)

conjunto3 = conjunto - conjunto1 #Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)

conjunto3 = conjunto1 - conjunto
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto #Elementos que no comparten o son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto | conjunto1
print(conjunto3)
print(conjunto1.issubset(conjunto3)) #ACA QUEREMOS VER SI EL CONJUNTO 1 ESTA DENTRO DEL CONJUNTO 3 Y ES TRUE

print(conjunto3.issuperset(conjunto1)) #ACA PREGUNTAMOS SI LOS ELEMENTOS DEL CONJUNTO 3 CONTIENEN LOS DEL 1
print(conjunto3.issuperset(conjunto))

#ACA VAMOS A VER SI AMBOS CONJUNTOS SON DISCONEXOS, QUE NO COMPARTEN NINGUN ELEMENTO EN COMUN
print(conjunto1.isdisjoint(conjunto))

#Convertir un conjunto en INMUTABLEEE
conjunto1 = frozenset



#***************************DICCIONARIO*************************************"
print("*******************DICCIONARIO********************")

#Son como los objetos de js

diccionario = {
    "ide": "pycharm",
    "Poo": 'Programacion orientada a objetos',
    "SABD": 'Sistema de administracion de base de datos'
}
print(diccionario)
print(len(diccionario))

print(diccionario['ide'])#Acceder a un diccionar con la llave
print(diccionario.get('Poo'))#Accedemos a la llave tambien con este metodo

diccionario['ide'] = 'Entorno de desarrollo integrado'
print(diccionario)

#como recorrer elementos ocn for

for i, valor in diccionario.items(): #Con el metodo ITEMS MOSTRAMOS TANTO LA LLAVE COMO EL VALOR DE LOS ELEMENTOS
    print(i, valor)

for llave in diccionario.keys():
    print(llave)

for valor in diccionario.values(): #Solo nos muestra los valores sin las llaves
    print(valor)

print('ide' in diccionario)#Devuelve un BOLEANO si esta o no esa llave
diccionario['PK'] = 'Primary key' #Con este metodo agregamos un key value nuevo
print(diccionario)

diccionario.pop("PK")#Metodo para retirar un elemento del objeto, pero si o si le tenemos que pasar el argumento
print(diccionario)

diccionario.clear()#Lo vaciamos
print(diccionario)
del diccionario #Lo eliminamos

# ***********************REPASO DICCIONARIOOOO**********************
diccionarioNuevo2 = {
    "Azul": "Blue",
    "Rojo": "Red",
    "Verde": "Green",
    "Amarillo": "Yellow"
}
print(diccionarioNuevo2)
del (diccionarioNuevo2['Azul'])
print(diccionarioNuevo2)

diccionarioNuevo3 = {
    "Ariel": {
        "Edad": 40,
        "Altura": 1.83,
    },
    "Osvaldo": [45, 1.85],
    "Natalia": [35, 1.65]
}
print(diccionarioNuevo3)
print(diccionarioNuevo3['Ariel']) #ACA MOSTRAMOS UNA KEY ESPECIAL

seleccionArg = {
    10: {'nombre': 'Leo Messi', 'edad': 35, 'altura': 1.70, 'precio': '$50 Millones', 'posicion': "extremo derecho"},
    11: {'nombre': 'Angel Di Maria', 'edad': 34, 'altura': 1.80, 'precio': '$12 Millones', 'posicion': "extremo derecho"},
    24: {'nombre': 'Paulo Dybala', 'edad': 28, 'altura': 1.77, 'precio': '$35 Millones', 'posicion': "media punta"},
    9: {'nombre': 'Julian Alvarez', 'edad': 22, 'altura': 1.73, 'precio': '$51 Millones', 'posicion': "delantero"},
    2: {'nombre': 'Cristian Romero', 'edad': 24, 'altura': 1.8, 'precio': '$48 Millones', 'posicion': "defensor central"},
    5: {'nombre': 'Leandro Paredes', 'edad': 28, 'altura': 1.80, 'precio': '$30 Millones', 'posicion': "medio campista"},
    20: {'nombre': 'Giovani Lo Celso', 'edad': 26, 'altura': 1.77, 'precio': '$22 Millones', 'posicion': "medio campista"}
}
for i, j in seleccionArg.items():
    print(i, j)

#*******************PILAS USANDO LISTAS*************************
print("*******************PILAS********************")
pila = [1, 2, 3]
#Agregamos el elemento al final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos el elemento del final
elementoPopeado = pila.pop()
print(pila)
print(elementoPopeado)

#*******************COLAS CON LISTAS*****************************
#FIFO(First in, first out)
print("*******************COLAS********************")
cola = ["Ariel","Naty","Pancho"]

cola.append("Yayo")
cola.append("Julian")
print(cola)
cola.pop(0)
print(cola)









