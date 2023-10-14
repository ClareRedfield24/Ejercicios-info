#Escribir un programa que pida al usuario un número entero y muestre por pantalla si 
#es positivo, negativo o cero

num = int(input("Por favor ingrese un numero entero: "))

if (num > 0):
    print("Su numero es positivo")
elif (num < 0):
    print("Su numero es negativo")
elif (num == 0):
    print("Su numero es igual a 0")
