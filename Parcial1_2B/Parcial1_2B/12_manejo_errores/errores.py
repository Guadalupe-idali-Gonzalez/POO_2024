#Los errores de ejecucion en un lenguaje de programacion se presenta cuando existen una anomalia dentro de la ejecucion del cpdigo, lo cual provoca que se detenga la ejecucion del SW con el control y manejo de excepciones sera posible minimizar o evitar la interrupcion del programa debido a una excepcion

#-------------------------------------------------------------------------------------------------------------------------------------
#Ejemplo 1. Cuando una variable no se genera 
# try:
#     nombre=input("Introduce el nombre completo de una persona: ")

#     if len(nombre)>0:
#         nombre_usuario="El nombre completo del usuario es: " + nombre

#     print(nombre_usuario)
# except:
#     print("Es necesario introducir un nombre de usuaior... Verifica por favor")
#-------------------------------------------------------------------------------------------------------
#Ejemplo 2, Cuando se solicita un numero y se ingresa otra cosa
# try:
#     numero=int(input("Ingresa un numero entero: "))

#     if numero>0:
#         print("Soy un numero entero positivo")
#     elif numero==0:
#         print("Soy un numero entero neutro")
#     else: 
#         print("Soy un numero entero negativo")
# except ValueError:
#     print("Ingresa un valor entero...")
#-------------------------------------------------------------------------------------------------------
#Ejemplo 3, Cuando se generan multiples excepciones
try:
    numero=int(input("Introduce un numero: "))
    print("El cuadrado es: " + str(numero*numero))
except ValueError:
    print("Introduce un valor entero numerico")
except TypeError:
    print("Se debe convertir el numero a entero")
else:
    print("No se presentaron errores de ejecucion")#De hoy en adelante 10/06/24 se usaran excepciones minimo
finally:
    print("Termine la ejecucion")