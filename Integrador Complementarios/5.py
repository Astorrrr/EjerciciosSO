stock = 0
diez = 0
articulos = 0

stock = int(input("Ingrese el stock: "))
diez = stock * 0.10

while True:
    articulos = int(input("Ingrese la cantidad  de articulos vendidos: "))
    stock -= articulos
    if stock > 0 and stock < diez:
        print("Queda menos del 10% del stock.")
    if stock <= 0:
        break

print("Se termino el stock.")    