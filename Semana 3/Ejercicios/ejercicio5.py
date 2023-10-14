# 5-Escribe un programa que imprima la suma de todos los números pares del 1 al
# 100.

suma = 0 
for numero in range(1,101):
    if (numero%2 == 0):
        suma +=numero
print(suma)

# otra forma de hacer
num = 0
pares = 2

while pares <= 100:
    num = num + pares
    pares = pares + 2
print(num)