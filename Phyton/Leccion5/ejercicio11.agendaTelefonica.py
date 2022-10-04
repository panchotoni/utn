guia = {}

print("Digite una opcion: \n 1 nuevo contacto \n 2 borrar contacto \n 3 ver contactos \n 4 salir \n")
ocpion = int(input("Digite un numero"))

while (ocpion != 4):
    if ocpion == 1:
        nombre = input("Digite el nombre")
        numer = input("Digite el numero")
        if nombre not in guia:
            guia[nombre] = numer
        else: print("Ya existe ese contacto")
    elif ocpion == 2:
        nombre = input("Digite el nombre de la persona que quiere borrar")
        if nombre in guia:
            del (guia[nombre])
        else:
            print("Este contacto no existe")
    elif ocpion == 3:
        for clave, valor in guia.items():
            print(clave, valor)
    ocpion = int(input("Digite otro numero"))








