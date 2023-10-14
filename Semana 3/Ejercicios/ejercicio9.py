# 9-Escribe un programa que pida al usuario un número y luego imprima la
# secuencia de Fibonacci correspondiente a ese número.


def fibonacci(n):
    secuencia = [0, 1]  # Inicializamos la secuencia de Fibonacci con los primeros dos números: 0 y 1

    if n <= 1:
        return secuencia[:n + 1]  # Si el número es 0 o 1, retornamos los primeros n + 1 elementos de la secuencia

    while len(secuencia) <= n +1:
        siguiente_numero = secuencia[-1] + secuencia[-2]  # Calculamos el siguiente número de la secuencia
        secuencia.append(siguiente_numero)  # Agregamos el siguiente número a la secuencia

    return secuencia

numero = int(input("Ingrese un número: "))

secuencia_fibonacci = fibonacci(numero)
print("La secuencia de Fibonacci hasta el número", numero, "es:")
print(secuencia_fibonacci)


    


    
