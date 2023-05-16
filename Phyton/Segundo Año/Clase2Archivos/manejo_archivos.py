try:
    archivo = open('prueba.txt', 'w', encoding='utf8') #La w es de write, a para modificar append, r para read, x exeption
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt. \n')
    archivo.write("Los acentos son imporantes para las palabras \n")
    archivo.write('Como por ejemplo: acción, ejecución y producción\n')
    archivo.write('Saludos al profe ariel\n')
    archivo.write('Con esto terminamos')
except:
    print(Exception)
finally: #Siempre se ejecuta.
    archivo.close()