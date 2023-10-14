#Escribir un programa que pida al usuario dos números y muestre por pantalla cuál de 
#ellos es mayor

num1 = int(input("Por favor ingrese el primer numero entero: "))
num2 = int(input("Por favor ingrese el segundo numero entero: "))

if (num1 > num2):
    print("El primer numero es mayor al segundo numero")
elif (num2 > num1):
    print("El segundo numero es mayor al primero")
else:
    print("Los numeros son equivalentes")
