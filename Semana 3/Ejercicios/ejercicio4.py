# 4-Escribe un programa que imprima los números pares del 1 al 100

num_pares = []


for i in range(1,100+2):  #Se le agrega el 2 para que tome el valor del 100
    if (i%2 == 0):
        num_pares.append(i)

print(num_pares)

# otra forma de hacer 
numero = 0
pares = 2
while numero <= 98:
    numero = numero + pares
    pares =pares + 0
    print(numero)
