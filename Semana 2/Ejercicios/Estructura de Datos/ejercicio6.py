# 6-Crear un set/conjunto con los números impares del 1 al 10 y mostrar el número
# de elementos en el conjunto.

numeros = {1,2,3,4,5,6,7,8,9,10}
numeros_impares = set()

for e in numeros:
    if (e%2 == 1):
        numeros_impares.add(e)

print("La cantidad de numeros impares son:",len(numeros_impares),"y ellos son:", numeros_impares)














