#IF / ELSE
'''condicion = "ASD"
if condicion == True:
    print("Condicion verdadera")
elif condicion == False:
    print("Condicion falsa")
else:
    print("Condicion sin especificar")
'''

num = int(input("Digite un numero del 1 al 3: "))
numText = ''
if num == 1:
    numText = "Numero uno"
elif num == 2:
    numText = "Numero dos"
elif num == 3:
    numText = "Numero tres"
else:
    numText = "Numero fuera del rango"
print(f'el numero ingresado es: {num} - {numText}')