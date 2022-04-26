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