print("Ingrese el tamaño del arreglo: ")
n = int(input())
vec = n*[""]

for i in range(n):
    vec[i] = input("Ingrese caracter: ")

z = ""
d = n

for i in range(n/2):
    z = vec[i]
    vec[i] = vec[d-1]
    vec[d-1] = z
    d = d-1

for i in range(n):
    print(vec[i])