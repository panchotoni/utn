def miFuncion():
    print("Mi primer funcion")

miFuncion()
miFuncion()
miFuncion()

def show(name, lastName):
    print(name + " " + lastName)

show("pancho", "toni")


numbers= [1,2,3,4,5]
for n in numbers:
    print(n)
else:
    print("Esto se termina")


#LIIST COMPREHENSION, LISTA DE COMPRENSIONNNN
names = ["pancho", "Julian", "Pamela", "Paola"]
alongP = [p for p in names if p[0] == "P"]
print(alongP)



botellas = [{"name": "Quilmes", "country": "Arg"},
            {"name": "Andes", "country": "Arg"},
            {"name": "Stella", "country": "Belgica"}]

arg = [i for i in botellas if i["country"] == "Arg"]
print(arg)

#VALORES POR DEFAULT EN FUNCIONES

def sumar (a = 0, b = 0):
    return a + b

resultado = sumar(1, 2)
print(resultado)


#Argumentos, variables en funciones

def listarNombres (*nombres):
    for i in nombres:
        print(i)

listarNombres("pancho", "lucas", "Jose")

def listaTerminos(**terminos): #Lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items():
        print(f"{llave} : {valor}")

listaTerminos(IDE = "integrated develoment enviroment" ,PK = "Primary key")


def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres123 = ["tito", "pedro", "carlos"]
desplegarNombres(nombres123)

#RECURSIVIDADDDDDDDDDDD

def factorial(nu):
    if(nu == 0):
        return 1
    else :
        return nu * factorial(nu-1)

factorial(5)