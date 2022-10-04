def impuestos (pago, impuesto):
    pago_total = pago + pago * (impuesto/100)
    return pago_total

valor = impuestos(1000, 21)
print(valor)
