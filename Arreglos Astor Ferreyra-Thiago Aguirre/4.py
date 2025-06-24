matrizA = []
matrizB = []
matrizC = []

print("Ingrese el tamaño de la matriz")
x = int(input("Filas: "))
y = int(input("Columnas: "))

for i in range(x):
    matrizA.append([])
    matrizB.append([])
    matrizC.append([])
    for j in range(y):
        matrizA[i].append(int(input("matrizA{},{}:".format(i+1,j+1))))
        matrizB[i].append(int(input("matrizB{},{}:".format(i+1,j+1))))
        matrizC[i].append(matrizA[i][j] + matrizB[i][j])

print(matrizA)
print(matrizB)
print(matrizC)