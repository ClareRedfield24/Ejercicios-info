# 11-Escribe un programa que pida al usuario un número y calcule su factorial.
# Un factorial es el producto que resulta de multiplicar un número entero positivo
# dado por todos los enteros inferiores a él hasta el uno. Por ejemplo, el factorial
# de 4 es 4! = 4 × 3 × 2 × 1 = 24.

num = int(input("Por favor ingrese un numero: "))

factorial = 1
 
if (num < 0):
    print("Lo siento, no se puede calcular el factorial de un numero negativo")
elif (num == 0):
    print("El factorial de cero es 1")
else: 
    for i in range(1,num+1):
        factorial = factorial*i
    print(f"El factorial del numero {num} es {factorial}")

  



