#Escribir un programa que pida al usuario un carácter y muestre por pantalla si
#es una letra mayúscula, una letra minúscula, un número o un carácter especial

caracter = input("Por favor ingrese un caracter: ")

if (caracter.islower()):
    print("El caracter es una letra minuscula")
elif (caracter.isupper()):
    print("El caracter es una letra mayuscula")
elif (caracter.isdigit()):
    print("El caracter es de un valor numerico")
else:
    print("Es un caracter especial")

