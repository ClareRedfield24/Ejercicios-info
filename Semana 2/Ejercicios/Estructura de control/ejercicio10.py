#Escribir un programa que pida al usuario una letra y muestre por pantalla si es
#una vocal o una consonante

letra = input("Por favor ingrese una letra: ")

if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
    print("La letra",letra,"es una vocal")
else:
    print("La letra",letra,"es una consonante")
    