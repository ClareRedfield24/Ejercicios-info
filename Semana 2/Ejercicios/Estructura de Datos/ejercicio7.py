# 7-Crear un diccionario con los nombres de tres ciudades y sus respectivas
# poblaciones. Agregar una cuarta ciudad al diccionario con su respectiva
# población. Mostrar el diccionario resultante

poblaciones_ciudades = {"Argentina": 40, "Paraguay": 39, "Bolivia": 45}

nueva_ciudad = input("Por favor ingresa una ciudad: ")
nueva_poblacion = int(input("Por favor ingresa su poblacion: "))

poblaciones_ciudades[nueva_ciudad]= nueva_poblacion

print(poblaciones_ciudades)

