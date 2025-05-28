treinta = 0
temp = 0
total = 0
mayor = 0

for i in range (7):
    temp = int(input("Ingrese la temperatura del dia de la semana: "))
    total += temp
    if temp > 30:
        treinta += 1
    if mayor <= temp:
        mayor = temp

promedio = total / 7

print("La media diaria es de: ", promedio)
print("La cantidad de dias que superaron los 30° fueron: ", treinta)
print("La mayor temperatura fue: ", mayor)