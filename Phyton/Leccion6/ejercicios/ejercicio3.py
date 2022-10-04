def imprimir(num):
    if num == 1:
        return print(num)
    else:
        print(num)
        imprimir(num - 1)

imprimir(5)