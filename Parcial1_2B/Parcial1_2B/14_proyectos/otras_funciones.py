def solicitarNumeros():
    n1=int(input("Coloca el numero 1:"))
    n2=int(input("Coloca el numero 2:"))
    return n1,n2
    

def operacionAritmetica(n1, n2, opcion):
        if opcion == '1' or opcion=='+' or opcion=='SUMA':
            return f"{n1}+{n2}={n1+n2}"
        elif opcion == '2' or opcion=='-' or opcion=='RESTA':
            return f"{n1}+{n2}={n1-n2}"
        elif opcion == '3' or opcion=='*' or opcion=='MULTIPLICACION' or opcion=='X':
            return f"{n1}+{n2}={n1*n2}"
        elif opcion == '4' or opcion=='/' or opcion=='DIVISION':
            return f"{n1}+{n2}={n1/n2}"
        elif opcion=='5' or opcion=='RAIZ':
            import math
            return n1
            math.sqrt(n1)
            print(n1)
        elif opcion =='6' or opcion=="POTENCIA":
            return f"{n1} a la potencia de {n2} = {n1**n2}"
        
        
def esperarTecla():
    print("Coloque cualquier tecla para continuar...")
    input()

def insertarPeliculas(peliculas):
    pelicula=input("Ingresa el nombre de la pelicula: ")
    peliculas.append(pelicula)
    espereTecla()

def eliminarPeliculas(peliculas):
    pelicula=input("Ingresa el nombre de la pelicula: ")
    for i in peliculas:
        if i==pelicula:
            print(f"Se elimino {pelicula}")
            peliculas.remove(pelicula)
    espereTecla()
    
def espereTecla():
    print("Coloque cualquier tecla para continuar...")
    input()
def actualizarLista(peliculas):
    pelicula=input("Actualiza la lista\n Coloca una nueva pelicula")
    peliculas.append(pelicula)
