print("CAJERO AUTOMATICO")
print("\n 1.Ingresar dinero \n 2.Retirar el dinero de la cuenta \n 3.Mostrar dinero disponible")
saldo = 1000
num = int(input("\nDigite una opcion"))
while(num != 4):
    if(num == 1):
        ingreso = int(input("Cuanto dinero quiere ingresar a la cuenta: "))
        saldo += ingreso
    elif(num == 2):
        retiro = int(input("Cuanto dinero quiere retirar: "))
        if (retiro > saldo):
                print("Saldo insuficiente")
        else:
            saldo -= retiro
    elif(num == 3):
        print(f"Su saldo es de {saldo}")

    num = int(input("\nDigite otra opcion"))

print("Muchas gracias nos vemos pronto")

