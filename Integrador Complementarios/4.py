aprobados = 0
desaprobados = 0

for i in range(10):
    nota = int(input("Ingrese la nota del alumno: "))
    if nota >= 6:
        aprobados += 1
    else:
        desaprobados += 1

print("Hubo", aprobados, "aprobados y", desaprobados,"desaprobados.")