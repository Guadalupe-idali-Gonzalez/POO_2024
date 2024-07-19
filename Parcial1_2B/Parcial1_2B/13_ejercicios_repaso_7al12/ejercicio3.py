# 3.- 

# Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#  palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#  el contenido de la lista en mayusculas

frases=[]
#checa que la lista esta vacia 
if not frases:
    print("La lista esta vacia")
    while True:
        entra = input("Introduce una palabra o frase")
        print("Para salir ingresa la palabra Salir: ")

        if entra.lower()== "salir":
            break

        frases.append(entra)
        print("Contenido de la lista.")

for item in frases:
    print(item.upper())