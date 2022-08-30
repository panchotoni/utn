'''
n = 3
print(n)
n = "HOLA MUNDO"
print(n)
n = 3.0
print(n)
x = 10
y = 2
z = x + y
print(z)
print(id(x))
# ID: Es el numero de memoria donde se guardan las variables, se muestras las ultimas 3 ej: x134,y cambian cada vez que se ejecuta.
#En una misma variable se pueden guardar un monton de datos y se van a mostrar todas y no es necesario que se identifiquen la variable



#MI GRUPO FAVORITO
miGrupoFavorito = "Patricio rey y los redonditos de ricota"+", "+"Soundgarden"
carac = "son buenas bandas"
print("Mi grupo favorito es: "+miGrupoFavorito, "porque",carac)

#INT PARA CADENAS

num1 = "5"
num2 = "6"
print(int(num1) + int(num2))

#TIPOS BOOLEANOS (BOOL)

miBooleano = 3 > 2
print(miBooleano)

#Si es verdadero entra directamente al primero, si es falso al ELSE>
if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")


#Ejercicios CAMPUS
dia = input("Como estuvo tu dia del 1 al 10?")
print("Mi dia estuvo de: ", dia)

titulo = input("Cual es el nombre del libro?")
autor = input("Cual es el autor del libro?")

print(titulo, "fue escrito por", autor)


operandoA = 8
operandoB = 5
suma = operandoB + operandoA
print("El resultado de la suma :", suma)
print(f"El resultado de la suma es: {suma} ")

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multi = operandoA * operandoB
print(f"La multiplicacion es: {multi}")

division = operandoA / operandoB
print(f"La division es igual a: {division}")
division = operandoA // operandoB
print(f"La division (int) es: {division}")

modulo = operandoA % operandoB
print(f"El residuo es de: {modulo}")

exponente = operandoA ** operandoB
print(f"El resultado es: {exponente}")


alto = int(input('Digite el valor de altura del rectangulo: '))
ancho = int(input('Digite el valor del ancho del rectangulo: '))
area = alto * ancho
perimetro = (alto + ancho) * 2
print('Area: ', area)
print('Perimetro', perimetro)


miVariable3 = 10
print(miVariable3)

# Operadores de reasignacion

miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

miVariable3 -= 2
print(miVariable3)

miVariable3 *= 3
print(miVariable3)

miVariable3 /= 2
print(int(miVariable3))


# Operadores de comparacion
d = 4
b = 4
resultado = d == b
print(resultado)

#Operador diferente
resultado = d != b
print(resultado)

#Operador Mayor o Menor
resultado = d > b
print(resultado)

#Menor o igual
resutlado = d <= b
print(resultado)


num = int(input('Digite un numero: '))
if num % 2 == 0:
    print(f'El numero {num} que ustedes selecciono es par')
else:
    print(f'El numero {num} que ustede selecciono es impar')


edad = int(input('Digite cual es su edad: '))
if edad >= 18:
    print(f'Su edad es de {edad} años, usted es mayor de edad')
else:
    print(f'Su edad es de {edad} años, usted es menor de edad')


num = int(input('Digite un numerito:'))
if num >= 0 and num <= 5:
     print(f"Su numero {num} esta entre el 0 y el 5")

else:
    print(f"Su numero {num} esta fuera del rango")


edad = int(input("Cual es su edad?: "))
if edad >= 20 and edad <= 30:
    print("La edad esta dentro del rango")
elif edad <20 or edad > 30:
    print("Fuera del rango")


num1 = int(input("Digite un numero: "))
num2 = int(input("Digite el segundu numero: "))

if num1 > num2:
    print(f"El numero mayorm es {num1}")
elif num1 < num2:
    print(f"El numero mayor es {num2}")
else:
    print("Los numeros son iguales")
'''
# print("Digite los datos del libro: ")
# nombre = input("Digite el nombre del libro: ")
# id = int(input("Digite el id del libro: "))
# precio = float(input("Digite el precio del libro: "))
# envioGratuito = (input("El envio es gratuito? Si o No: "))
# if envioGratuito == "Si":
#     envioGratuito = True
# elif envioGratuito == "No":
#     envioGratuito = False
# else:
#     envioGratuito = "El dato ingresado es incorrecto, ingrese SI O NO"
# print(f"""
#         Nombre: {nombre}
#         id: {id}
#         Precio: {precio}
#         Envio gratuito: {envioGratuito}
""")