presupuesto = 20000

while True:
    compra = int(input("Ingrese el valor de la compra: "))
    if compra > presupuesto:
        print("No alcanza el presupuesto.")
        break
    presupuesto -= compra
    if presupuesto <= 0:
        print("Se termino el presupuesto.")
        break
    print("Queda", presupuesto, "de presupuesto.")


print("Se termino el stock.")