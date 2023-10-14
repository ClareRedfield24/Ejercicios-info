# 13-Escribe un programa que pida al usuario un número y luego imprima un
# triángulo de asteriscos con esa cantidad de filas.
# *
# **
# ***
# ****
# *****

num_filas = int(input("Por favor ingrese el numero de filas que desea realizar : "))

for i in range(1,num_filas+1):
    print("*"*i)


