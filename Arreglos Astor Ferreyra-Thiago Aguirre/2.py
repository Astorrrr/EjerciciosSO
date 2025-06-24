c = 0
suma = 0
media = 0
temp = []

print("Ingrese la cantidad de temperaturas: ")
n = int(input())

for i in range(n):
    temperatura = float(input("Ingrese la temperatura {0}:".format(i+1)))
    temp.append(temperatura)
    suma += temp[i]

media = suma / n


for i in range(temp):
    if i >= media:
        c += 1
        print(i)