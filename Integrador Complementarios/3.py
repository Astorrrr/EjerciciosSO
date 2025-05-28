cont = 0
agua = 0
total = 0
promedio = 0

for i in range (7):
    cont  += 1
    agua = int(input("Ingrese cuantos vasos de agua tomaste en el dia", cont,"de la semana: "))
    total += agua

promedio = total / 7

print("El promedio diario es de: ", promedio)
if total < 8:
    print("Se recomienda aumentar su consumo de agua")