matrizA = []

print("Ingrese el tamaño del arreglo: ")
N = int( input())

if 1 <= N and N <= 100:

    for i in range(N):
        matrizA.append([])
    for j in range(N):
        elemento = input("matrizA{}{}: ".format(i, j))
        matrizA[i].append(int(elemento))
BAND = True
i = 0
while i < N and BAND == True:
    j = 0
    while j < i-1 and BAND == True:
        if matrizA[i][j] == matrizA[j][i]:
            j = j + 1
        else:
            BAND = False
            i = i + 1
    if BAND:
        print("Es simetrica.")
    else:
        print("No es simetrica.")
else:
    print("El tamaño de la matriz no es valido.")