# 14-Escribe un programa que pida al usuario un número y luego imprima un
# triángulo de números como el siguiente:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

num_filas = int(input("Por favor ingrese el numero de filas que desea: "))
fila = 1
for i in range(1,num_filas+1):
    for j in range(fila):
        print(fila,end=" ")
    fila += 1
    print()



