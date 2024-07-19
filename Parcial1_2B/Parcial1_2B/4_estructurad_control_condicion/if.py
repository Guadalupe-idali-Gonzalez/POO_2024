#esta estructura de control evalua una condicion, si la condicion se cumple se ejecuta la o las instrucciones contenidas dentro de ella esta.

#Esta estructura tiene 4 variantes
#1 If simple
#2 If compuesto
#3 If anidado
#4 If con el elif

#Ejemplo 1 if simple

color="rojo"

if color=="rojo":
    print("Soy el color rojo")

#If compuesto

color="rojo"

if color=="rojo":
    print("Soy el color rojo")
else:
    print("No soy el color rojo")


#Ejemplo 3 If anidado

color="rojo"

if color=="rojo":
    print("Soy el color rojo")
if color!="rojo":
    print("No soy rojo")
else:
    print("No soy el color rojo")

#ejemplo 4 if y elif

color=input("Ingresa el color: ")

if color=="rojo":
    print("Soy el color rojo")
elif color=="amarillo":
    print("Soy el color amarillo") 
elif color=="azul":
    print("Soy el color azul")
elif color=="negro":
    print("Soy el color negro")
else:
    print("no soy ninguno de los colores anteriores")
