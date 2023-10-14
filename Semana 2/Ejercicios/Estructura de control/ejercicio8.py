#Escribir un programa que pida al usuario una cadena de caracteres y muestre por pantalla 
#si contiene la letra "a"

def controldepalabra():   
    palabra = input("Introduce unas plabras: ")

    if ("a" in palabra.lower()):        
        print("Contiene la letra A y/o a")
    else:
        print("No contiene la leta A y/o a")

controldepalabra ()

#Lo que se hace es tranformar en una funcion

#al agregar la palabra lower lo que se hace es tranformar el caracter 
#que se ponga en mayuscula en minuscula