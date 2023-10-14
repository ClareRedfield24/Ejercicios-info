# 19-Escribe un programa que pida al usuario un número y luego imprima si ese
# número es un número perfecto o no. Un número perfecto es aquel que es igual a
# la suma de sus divisores propios (excluyendo el propio número).
# Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se
# puede dividir por 1, 2 y 3, y cuando sumas esos números, el resultado es 6

def perfecto(num):
    divisores = []
    for i in range(1,num):
        if (num % i == 0):
            divisores.append(i)
    
    if (num == sum(divisores)):
        return "es perfecto"
    else:
        return "no es perfecto"
    

numero = int(input("Por favor ingrese un numero: "))

print(f"El numero {numero}: {perfecto(numero)}")

