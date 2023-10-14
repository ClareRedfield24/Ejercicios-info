# 3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
# multiplicar correspondiente a ese número del 1 al 10.

num = int(input("Por favor ingrese un numero del cual desea obtener su tabla de multiplicar:"))

multiplicacion = 0
multiplo = 1

while multiplo <= 10:
    multiplicacion = num * multiplo
    multiplo = multiplo + 1

    print(multiplicacion)

#otra forma de hacer
num = int(input("Por favor ingrese un numero del cual desea obtener su tabla de multiplicar: "))

multi = 1
for i in range(1,11):
    multi = num * i
    print(multi)

