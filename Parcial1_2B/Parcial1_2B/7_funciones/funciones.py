#Una funcion es un conjunto de instrucciones agrupadas bajo un nombre particular como un programa mas pequeño que cumple una funcion especifica. La funciopn se puede reutilizar con el simple hecho de invocarla, es decir, mandarla a llamar.

#Sintaxis


# def nombredeMiFuncion(parametros):
#     bloque o conjunto de instrucciones

#nombredeMifuncion(parametros)

#Las funciones pueden ser de 4 tipos
#1.- Funcion que no recibe parametros y no regresa valor
#2.- Funcion que no recibe parametros y regresa valor
#3.- Funcion que recibe parametros y no regresa valor
#4.- Funcion que recibe parametros y regresa valor



#Ejemplo 1: crear una funcion para imprimir nombres de personas.
#Funcion que no recibe parametros y no regresa valor
def solicitarNombres():
    nombre=input("Ingresa el nombre completo: ")

solicitarNombres()

#Ejemplo2
def suma():
    numero1=int(input("Numero #1: "))
    numero2=int(input("Numero #2: "))
    suma=numero1+numero2
    print(f"{numero1}+{numero2}={suma}")
suma()

#ejemplo3
#2.- Funcion que no recibe parametros y regresa valor
def suma():
    numero1=int(input("Numero #1: "))
    numero2=int(input("Numero #2: "))
    suma=numero1+numero2
    return suma

resultado_suma=suma()
print(f"La suma es: {suma()}")
print(f"La suma es: {resultado_suma}")

#Ejemplo 4
#3.- Funcion que recibe parametros y no regresa valor
def suma(num1,num2):
    suma=num1+num2
    print(f"La suma es: {suma}")

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
suma(n1,n2)

#Ejemplo 5
#4.- Funcion que recibe parametros y regresa valor
def suma(num1,num2):
    suma=num1+num2
    return suma

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
resultado_suma=suma(n1,n2)
print(f"La suma es: {resultado_suma}")
#print(f"{n1} + {n2} = {suma(n1,n2)}")

#eje 6: crear un programa que solicite a traves de una funcion la siguiente informacion: Nombre del paciente, edad, estatura, tipo de sangre. Utilizar los 4 tipos de funciones.

#1 no regresa valor y no pide parametros
#una funcion es como un metodo, solo que sin crear clases 
def solicitarPaciente1():
    nombre=input("Nombre del paciente: ")
    edad=int(input("edad del paciente: "))
    estatura=float(input("Estatura: "))
    tipo_sangre=input("Tipo de sangre: ")

    print(f"Nombre del paciente {nombre} Edad: {edad}  estatura{estatura} tipo de sangre{tipo_sangre}")
for i in range(1,4):
    solicitarPaciente1()

#2 Funcion no tiene parametros y regresa valor
def solicitarPaciente2():
    nombre=input("Nombre del paciente: ")
    edad=int(input("edad del paciente: "))
    estatura=float(input("Estatura: "))
    tipo_sangre=input("Tipo de sangre: ")
    
    return f"Nombre del paciente {nombre} Edad: {edad}  estatura{estatura} tipo de sangre{tipo_sangre}"

print(solicitarPaciente1())

#3 Funcion  tiene parametros y no regresa valor
def solicitarPaciente3(nom, ed, est, sangre):
    print(f"Nombre del paciente {nombre} Edad: {edad}  estatura{estatura} tipo de sangre{tipo_sangre}")
nombre=input("Nombre del paciente: ")
edad=int(input("edad del paciente: "))
estatura=float(input("Estatura: "))
tipo_sangre=input("Tipo de sangre: ")
    
solicitarPaciente3(nombre, edad, estatura, tipo_sangre)

#4 Funcion  tiene parametros y regresa valor
def solicitarPaciente3(nom, ed, est, sangre):
    return f"Nombre del paciente {nombre} Edad: {edad}  estatura{estatura} tipo de sangre{tipo_sangre}"
nombre=input("Nombre del paciente: ")
edad=int(input("edad del paciente: "))
estatura=float(input("Estatura: "))
tipo_sangre=input("Tipo de sangre: ")
    
print(solicitarPaciente3(nombre, edad, estatura, tipo_sangre))
