vect = []
n = int(input("Ingrese el numero de elementos: "))

if n >= 1 and n <= 200:
    for i in range(1, n+1):
        elemento = int(input("Ingrese el entero {0}:".format(i)))
        vect.append(elemento)
i = 0

lista = []
for elemento in vect:
    if elemento not in lista:
        lista.append(elemento)

lista.sort()

print(lista)

