# 18-Escribe un programa que pida al usuario un número y luego imprima un
# triángulo de números como el siguiente:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

num_filas = int(input("Por favor ingrese el numero de filas que desea: "))

num =1

for i in range(1,num_filas+1):
    for j in range(1, i+1):
        print(num,end=" ")
        num +=1
    print()

