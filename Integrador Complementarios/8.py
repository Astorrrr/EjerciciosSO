cont=0
total=1
i=1
for i in range(7):
    cant=int(input("Ingrese la cantidad de minutos que usted realiza ejercicio en un día: "))
    cont=cont+1
    total=cant+total


prom=total/cont

if prom<30:
    print("usted deberia aumentar la actividad")
else:
    print("no necesita aumentar la cantidad de tiempo si no quiere")
