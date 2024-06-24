#Los errores de ejecucion en un lenguaje de programacion se presentan cuando exixte una anomalia dentro de la ejecucion del codigo lo cual provoca que se detenga la ejecucion del SW, con el control y manejo de exepciones sera posible minimizar o evitar la interupcciondel programa debido a una excepcion.

#Ejemplo 1. cuando una bariable no se genera

try:
    nombre=input("Introduce el nombre completo de una persona: ")

    if len(nombre)>0:
        nombre_usuario="El nombre completo del usuario es: "+nombre
    
    print(nombre_usuario)
    print 
    (len(nombre_usuario))
except:
    print("Es necesario introducir un nombre de usuario...Verifica por favor")
    
x=3+4
print("El valor de x es: "+str(x))

#Ejemplo 2. Cuando se solicita un numero y se ingresa otra cosa

try:
    numero=int(input("Ingrese un numero: "))

    if numero>0:
        print("Soy un numero entero positivo")
    elif numero==0:
        print("Soy un numero entero neutro")
    else:
        print("Soy un numero entero negativo")
except ValueError:
    print ("Introduce un valor numerico positivo")
    
#Ejemplo 3 generan multiples excepciones

try:
    numero=int(input("Introduce un numero: "))

    print("El cuadrado del numero es: "+str(numero*numero))
except ValueError:
    print("Introduce un valor numerico entero")
except TypeError:
    print("Se debe convertir el numero a entero")
else:
    print("Todo bien")
finally:
    print("Termine la ejecucion")
    