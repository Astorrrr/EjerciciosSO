total = 0
carga = 1
menor = False
cont = 0
promedio = 0

while carga != 0:
    carga = int(input("Ingrese la carga de combustible en litros (0 para salir): "))
    total += carga
    if carga <= 5:
        menor == True
    cont += 1

print(cont)
print(total)
promedio = total / cont
print(promedio)

print("El total de las recargas fue: ", total, "litros.")
print("El promedio de las recargas fue: ", promedio, "litros.")

if menor == True:
    print("Hubo una o mas cargas menores a 5 litros (sospecha de error o recarga minima).")
