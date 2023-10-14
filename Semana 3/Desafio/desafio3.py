#Desafío 3: Adivina el número

# Vamos a crear un juego completamente funcional.
# Para ello el programa debe:
# Pedir al usuario que ingrese su nombre.
# Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos para adivinarlo.
# Generar aleatoriamente un número entero entre 1 y 100
# Informarle al usuario cuántos intentos le quedan y solicitarle que ingrese un número

nombre = input("Por favor ingrese su nombre: ")

#tip 1: importar de la biblioteca random la función randint (Tu profe te explicará en clase cómo hacerlo)
import random  

def adivinar_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 8

    while intentos > 0:
        print("Le quedan",intentos,"intentos")
        num_usuario = input("Adivina el número (entre 1 y 100): ")

#tip 2: con el método isdigit() puedes saber si es posible convertir a entero
        if not num_usuario.isdigit():
            print("Por favor ingrese un numero entero: ")
            continue
#Si el usuario no ingresa un número entero no debes descontarle un intento, en los demás casos si
# debes descontarle un intento
        numero_entero = int(num_usuario)

#En cada intento debes informarle al usuario los intentos que le quedan disponibles y solicitarle que 
#ingrese otro número.
# Ser menor al que tiene que adivinar, en éste caso informarle que el número a adivinar es mayor.
# Ser mayor al que tiene que adivinar, en éste caso informarle que el número a adivinar es menor.
# Igual al que tiene que adivinar, en éste caso informarle que ha ganado y decirle en cuál intento 
# lo adivinó.

        if (numero_entero < numero_secreto):
            print("Demasiado bajo. Intenta nuevamente")
        elif (numero_entero > numero_secreto):
            print("Demasiado alto. Intenta nuevamente")
        else:
            print(f"¡Felicitaciones {nombre}! ¡Adivinaste el número en el {9-intentos} intento!")
            break
        intentos -= 1

#Si el usuario no acierta en los 8 intentos, debes informarle que se agotaron los intentos y cuál era el 
#número que tenía que adivinar
    print(f"¡Lo siento {nombre}! El número secreto era {numero_secreto}. Has agotado tus 8 intentos.")
        
adivinar_numero()


