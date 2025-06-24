total=0

while True:
    cargas = int(input("Ingrese las cargas de combustible en este vehículo (0 para cerrar el programa): "))
    total = total + cargas
    if cargas == 0:
        break

km = total/0.07

if km <50:
    print("no queda suficiente combustible para recorrer 50km")
elif km >= 50:
    print("queda suficiente combustible para recorrer 50km")
