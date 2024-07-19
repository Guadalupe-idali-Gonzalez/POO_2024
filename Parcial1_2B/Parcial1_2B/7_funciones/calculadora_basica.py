
# opcion=True
# while opcion:
#     print("--Calculadora Basica--\n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.-Division \n 5.-SALIR" )
#     opcion=input("\t elige una opcion: ").upper()
#     if opcion == '1' or opcion=='+' or opcion=='SUMA':
#         n1=int(input("Coloca el numero 1:"))
#         n2=int(input("Coloca el numero 2:"))
#         print(f"{n1}+{n2}={n1+n2}")
#     elif opcion == '2' or opcion=='-' or opcion=='RESTA':
#         n1=int(input("Coloca el numero 1:"))
#         n2=int(input("Coloca el numero 2:"))
#         print(f"{n1}-{n2}={n1-n2}")
#     elif opcion == '3' or opcion=='*' or opcion=='MULTIPLICACION' or opcion=='X':
#         n1=int(input("Coloca el numero 1:"))
#         n2=int(input("Coloca el numero 2:"))
#         print(f"{n1}*{n2}={n1*n2}")
#     elif opcion == '4' or opcion=='/' or opcion=='DIVISION':
#         n1=int(input("Coloca el numero 1:"))
#         n2=int(input("Coloca el numero 2:"))
#         print(f"{n1}/{n2}={n1/n2}")
#     else: 
#         print("Terminaste la ejecucion del SW")
#         opcion=False


import os
from otras_funciones import *
#def solicitarNumeros():
#     global n1,n2
#     n1=int(input("Coloca el numero 1:"))
#     n2=int(input("Coloca el numero 2:"))
    

# def operacionAritmetica(num1, num2, ope):
#         if opcion == '1' or opcion=='+' or opcion=='SUMA':
#             return f"{n1}+{n2}={n1+n2}"
#         elif opcion == '2' or opcion=='-' or opcion=='RESTA':
#             return f"{n1}+{n2}={n1-n2}"
#         elif opcion == '3' or opcion=='*' or opcion=='MULTIPLICACION' or opcion=='X':
#             return f"{n1}+{n2}={n1*n2}"
#         elif opcion == '4' or opcion=='/' or opcion=='DIVISION':
#             return f"{n1}+{n2}={n1/n2}"
        
# def esperarTecla():
#     print("Coloque cualquier tecla para continuar...")
#     input()
    

opcion=True
while opcion:
    os.system("clear")
    print("--Calculadora Basica--\n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.-Division \n 5.-SALIR" )
    opcion=input("\t elige una opcion: ").upper()
    if opcion != '5':
        n1,n2=solicitarNumeros()
        print(operacionAritmetica(n1,n2,opcion))
    else:
        opcion=False
        print("Terminaste el SW")

 
    