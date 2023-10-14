# 7-Escribe un programa que pida al usuario una palabra y determine si es un
# palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
# izquierda).

palabra = input("Por favor ingrese una palabra: ")

palabra_minus = palabra.lower() #Convertimos a minusculas 
palabra_reversa = palabra_minus[::-1]

if (palabra_minus == palabra_reversa):
    print("Tu palabra",palabra,"es un palíndromo")
else:
    print("Tu palabra",palabra,"no es un palíndromo")


