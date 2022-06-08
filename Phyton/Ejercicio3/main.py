print ("Digite un mes del año del 1 al 12")
mes = int(input("Digite el numero: "))

while mes<1 or mes>12:
   print ("Fuera de rango")
   mes = int(input("Digite el numero: "))

if mes >= 1 and mes <= 3:
    print("La estacion del año es Verano")
elif mes >= 4 and mes <= 6:
    print("La estacion del año es otoño")
elif mes >= 7 and mes <= 9:
    print("La estacion del año es invierno")
elif mes >= 10 and mes <= 12:
    print("La estacion del año es primavera")
