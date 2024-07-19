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
        
def esperarTecla():
    print("Coloque cualquier tecla para continuar...")
    input()
