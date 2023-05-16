from ManejoArchivos import ManejoArchivos
#Manejo de contexto con WITH: abre y cierra el archivo solo
#with open('prueba.txt', 'r', encoding='utf8') as archivo:
#    print(archivo.read())
#No hace falta ni el try ni el finally
#Utiliza metodos como __enter__ que abre y __exit__ que cierra

with ManejoArchivos('prueba.txt') as archivo:
    print((archivo.read()))
