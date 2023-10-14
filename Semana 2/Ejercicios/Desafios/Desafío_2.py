#Desafío 2: Analizador de textos
#Se te pide crear un programa que le pida al usuario que ingresar un texto cualquiera, por ejemplo, un artículo o una frase.
    #Luego el programa le va a pedir al usuario que también ingrese 3 letras a su elección.
    #Nuestro código va a procesar esa información para realizar los análisis necesarios para devolverle al usuario la siguiente información:

        ##Solicitar Datos
texto= input("Ingresa el texto a analizar: ")

    # Cantidad de veces que aparece las letras que eligió
# Tip 1: almacenar las letras en una lista para usar algún método de contar un substring en un string
# Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar que se encuentren todas las letras, pasa tanto el texto original como las letras a buscar a minúscula.
letra1= input("Ingrese la 1era de las letras a analizar del texto: ")
letra2= input("Ingrese la 2da de las letras a analizar del texto: ")
letra3= input("Ingrese la 3era de las letras a analizar del texto: ")


texto=texto.lower()
letras=[letra1.lower(), letra2.lower(), letra3.lower()]

for letra in letras:
 print(f"La letra {letra} apareció {texto.count(letra)} veces")
 

# Cuantas palabras hay en total en todo el texto
# Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular su longitud.
palabras= texto.split(" ")
print("La cantidad de palabras que hay en el texto es", len(palabras))

# Cual es la primera letra y cuál es la última
print("La primera letra es: {palabras[0]}", "La última letra es: {palabras[-1]}")

# Mostrar el texto en orden inverso
texto_reversa= palabras[::-1]
print("El texto en orden inverso es:", texto_reversa)

# Decir si la palabra "python" aparece en el texto
# Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un string para mostrar al usuario.
diccionario= {True:"Si hay en el texto", False:"No hay en el texto"}
python_esta_o_no= "python" in texto
print(diccionario[python_esta_o_no], "la palabra python ")