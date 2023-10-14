# 16-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# la misma cadena pero con cada palabra al revés.

texto = input("Por favor ingrese un texto: ")
texto = texto.split(" ")
lista_reverso = []

for palabras in texto:
    lista_reverso.append(palabras[::-1])

texto_reverso = " ".join(lista_reverso)


print(f"El texto con cada palabra revertifa es {texto_reverso}")
