#Una funcion es un conjunto de instruccioneds agrupadas bajo un nombre en particular como un programa
#particular como un programa mas pequeño que cumple una funcion especifica. La
#funcion se puede reutilizar con el simple hecho de invocarla, es decir, mandarla llamar.

#Sintaxis

def nombredeMifuncion():
   # bloque o conjunto de instrucciones
   print("hola")
    
nombredeMifuncion()

#Las funciones pueden ser de 4 tipos 
#1.-Funcion que no recibe parametros y no regresar valor
#2.-Funcion que no recibe parametros y regresa valor
#3.-Funcion que recibe parametros y no regresa valor
#4.-Funcion que recibe parametros y regresa valor


    #1.-Funcion que no recibe parametros y no regresar valor
#Ejemplo- Crear una funcion para imprimir nombres de personas

def solicitarNombres():
    nombre=input("Ingrese el nombre completo: ")
    
solicitarNombres()

#Ejemplo2 - funcion que realiza sumatoria

def suma():
    n1=int(input("Numero #1"))
    n2=int (input("Numero #2"))
    suma=n1+n2
    print(f"{n1} + {n2} = {suma}")
    
suma()

    #2.- Funcion que no recibe parametros y regresa valor
#Ejemplo 3 - funcion que realiza sumatoria de dos numeros

def suma():
    n1=int(input("Numero #1"))
    n2=int (input("Numero #2"))
    suma=n1+n2
    return suma

resultado_suma=suma()
print(f"LA suma es: {suma()}")
print(f"LA suma es: {resultado_suma}")

    #3.-Funcion que recibe parametros y no regresa valor
#Ejemplo 4 - funcion que realiza sumatoria de dos numeros

def suma(n1,n2):

    suma=n1+n2
    print(f"LA suma es: {suma}")



n1=int(input("Numero #1: "))
n2=int (input("Numero #2: "))
    
suma(n1,n2)


    #4.-Funcion que recibe parametros y regresa valor
#Ejemplo 5 - funcion que realiza sumatoria de dos numeros

def suma(n1,n2):

    suma=n1+n2
    return suma



n1=int(input("Numero #1: "))
n2=int (input("Numero #2: "))

resultado_suma=suma(n1,n2)
print(f"La suma es: {resultado_suma}")


#Ejemplo 6- crear un programa que solicite a traves
#de una funcion la siguiente informacion: 
# Nombre del paciente, edad, estatura, tipo de sangre.
#utilizar los 4 tipos de funciones






