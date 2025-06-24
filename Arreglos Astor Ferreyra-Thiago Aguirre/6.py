monto = []
print("Ingrese número de sucursales y años: ")
N = int( input("Número de Sucursales: "))
M = int( input("Número de Años: "))
for i in range(M):
    monto.append([])
    for j in range(N):
        print("Ingrese ventas de la sucursal", j+1 , "en el año", i+1 )
        venta = int( input())
        monto[i].append(venta)


print("Sucursal con mas ventas: ")
max = 0
for j in range(N):
    suma = 0
    for i in range(M):
        suma = suma + monto[i][j]
    print ("Número de ventas de la Sucursal" , j+1, "es", suma)
    if suma > max :
        max = suma
        SUC = j + 1
print("Sucursal que más vendió: ", SUC)
print("Promedio de ventas: ")


max = 0
for i in range(M):
    suma = 0
    for j in range(N):
        suma = suma + monto[i][j]
    Prom = suma/N
    print ("Promedio de ventas del año" , i+1, "es", Prom)
    if Prom > max :
        max = Prom
        año = i + 1 
        print("Año con mayor Promedio", año)