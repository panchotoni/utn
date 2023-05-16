archivo = open('prueba.txt', 'r', encoding='utf8')
# print(archivo.read())
# print(archivo.read(15)) #Para que lea hasta ciertos caracteres
#print(archivo.readline())

#Iteramos el archivo, cada unas de las lineas
#for linea in archivo:
    #print(linea) Iteramos todas las lineas de la lista
    #print(archivo.readlines()) Iteramos y lo guardamos en una lista

#ANEXAMOS INFORMACION, COPIAS a otro

archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())
archivo.close()
archivo2.close()

print('Se ha terminado el proceso de leer y copiar archivos')