total = 0
mayor = 0
cantidad = 0

while True:
    donacion = int(input("Ingrese la donacion (0 para salir):"))
    if donacion == 0:
        break
    cantidad += 1
    total += donacion
    if donacion > mayor:
        mayor = donacion

print("El total de las donaciones es: ", total)
print("La cantidad de las donaciones es: ", cantidad)
print("La mayor de las donaciones fue: ", mayor)