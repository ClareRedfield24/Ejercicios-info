#Escribir un programa que pida al usuario un número entero y muestre por pantalla 
#si es múltiplo de 2 y de 3 a la vez

num = int(input("Por favor ingrese un numero entero: "))

if ((num%2 == 0) and (num%3 == 0)):
    print("Su numero es multiplo de 2 y 3 a la vez")
else:
    print("Su numero NO es multiplo de 2 y 3")
