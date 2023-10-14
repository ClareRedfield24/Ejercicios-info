# 2-Escribe un programa que pida al usuario un número y calcule la suma de todos
# los números naturales del 1 hasta ese número.


cont = 0 #Contador 1 + 1
suma = 0  
num = int(input("Por favor ingrese un numero: "))

while cont <= num:
    suma = suma + cont
    cont = cont + 1
print("La suma total es:",suma)

#otra forma de hacer
suma = 0
for i in range(1,num+1):
    suma = suma + i
print("La suma total es:",suma)




