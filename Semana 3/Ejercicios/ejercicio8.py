# 8-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# el número de palabras que contiene.

texto = input("Por favor ingrese un texto: ")

texto_lista = texto.split(" ")
num_palabras = len(texto_lista)


print("La cantidad de palabras en tu texto es de",num_palabras)

