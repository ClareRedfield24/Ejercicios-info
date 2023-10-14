# 10-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# la misma cadena pero con todas las vocales en mayúscula.

def convertir_vocales_en_mayusculas (cadena):
    vocales = ["a","e","i","o","u"]
    resultado = " "

    for letra in cadena:
        if (letra.lower() in vocales):
            letra = letra.upper()
        resultado += letra
    return resultado

texto = input("Por favor ingrese una cadena de texto: ")
print("El texto original es:",texto)
texto_convertido = convertir_vocales_en_mayusculas(texto)
print("El texto con las vocales convertidas en mayuscula es:", texto_convertido)

