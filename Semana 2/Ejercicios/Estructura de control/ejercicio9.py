#Escribir un programa que pida al usuario tres números y muestre por pantalla
#el mayor de ellos

primer_valor = int(input("Ingrese un numero: "))
segundo_valor = int(input("Ingrese un segundo numero: "))
tercer_valor = int(input("Ingrese un tercer numero: "))

if (primer_valor > segundo_valor and primer_valor > tercer_valor):
    print("El numero mayor es el",primer_valor)
            
elif (segundo_valor > tercer_valor and segundo_valor > primer_valor):
    print("El numero mayor es:",segundo_valor)

elif (tercer_valor > segundo_valor and tercer_valor > primer_valor):
    print("El mayor valor es:",tercer_valor)

else:
    print("Los tres valores son iguales")
    


