i = 1
vec = []

print("Ingrese la cantidad de elementos para ingresar: ")
elementos = int(input())

while i <= elementos:
    elemento = int(input("Ingrese el elemento: "))
    vec.append(elemento)
    i += 1

print(vec)