# 17-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# la misma cadena pero con las palabras en orden inverso.

texto= input("Ingresa uan cadena de texto: ")
texto=texto.lower()
palabras= texto.split(" ")
# Mostrar el texto en orden inverso
texto_reversa= palabras[::-1]
texto_reversa = " ".join(texto_reversa)
print("El texto en orden inverso es:", texto_reversa)

