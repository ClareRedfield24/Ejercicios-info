# 15-Escribe un programa que pida al usuario una cadena de texto y determine
# cuántas veces aparece cada letra en la cadena.

texto = input("Por favor ingrese una cadena de textos: ")
texto = texto.split(" ")
texto = "".join(texto)

frecuencia_letras = {} #se crea un diccionario llamado 
#frecuencia_letras para almacenar la frecuencia de cada letra en la cadena. 
# Cada letra encontrada se convierte en una clave del diccionario, y su valor 
# correspondiente es la cantidad de veces que aparece en la cadena.

for letra in texto:
    if (letra in frecuencia_letras):
        frecuencia_letras[letra] +=1 # Si la letra ya está presente en el diccionario, se incrementa su frecuencia en 1
    else:
        frecuencia_letras[letra] = 1 #de lo contrario agrega esa letra con el valor de 1

print("Frecuencia de letras en la cadena: ")
print(frecuencia_letras)


