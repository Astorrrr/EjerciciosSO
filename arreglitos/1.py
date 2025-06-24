vec1 = 3*[0]
vec2 = 3*[0]
sum = 0


for i in range(3):
    vec1[i] = int(input("vec1({}): ".format(i+1)))
for i in range(3):
    vec2[i] = int(input("vec2({}): ".format(i+1)))

for i in range(3):
    prod = vec1[i]*vec2[i]
    sum =  sum + prod

print("El producto escalar es: ", sum)

x = vec1[1]* vec2[2] - vec1[2]* vec2[1]
y = -( vec1[0]* vec2[2] - vec1[2]* vec2[0] )
z = vec1[0]* vec2[1] - vec1[1]* vec2[0]

print("El producto vectorial es: {}i {}j {}k".format(x, y, z))