gastos = 0
gasto = 1
limite = 25000

while gasto != 0:
    gasto = int(input("Ingrese sus gastos del mes (0 para salir): "))
    gastos += gasto

if gastos >= limite:
    print("Los gastos (",gastos, ") superan al presupuesto (", limite, ")")
else:
    print("Los gastos (",gastos, ") no superan al presupuesto (", limite, ")")