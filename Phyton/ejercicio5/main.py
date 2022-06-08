nota = float(input("Digite su nota"))

while nota < 0 or nota > 10:
    print("Nota inexistente, vuelva a digitar")
    float(input("Digite su nota"))

if nota <= 10 and nota >= 9:
    print("Su calificacion es A")
elif nota >=8 and nota < 9:
    print("Su calificacion es B")
elif nota >=7 and nota < 8:
    print("Su calificacion es C")
elif nota >=6 and nota < 7:
    print("Su calificacion es F")
else:
    print("El valor es incorrecto")
