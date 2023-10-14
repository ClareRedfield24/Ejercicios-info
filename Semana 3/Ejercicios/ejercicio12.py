# 12-Escribe un programa que pida al usuario una lista de números separados por
# comas y calcule su promedio

numeros = input("Por favor ingrese una lista de numeros separados por coma:")

lista_numeros =[float(num) for num in numeros.split(",")]

suma = 0

def suma_lista (lista):
    suma = 0
    for i in lista:
        suma = suma + i
        
    return suma

def promedio (lista):
    return suma_lista(lista)/len(lista)
   
print(f" El pomedio de su lista de numeros es {promedio(lista_numeros)}")

