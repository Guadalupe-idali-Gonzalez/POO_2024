import os

# def solicitarNumeros():
#   global n1,n2  
#   n1=int(input("Numero #1: "))
#   n2=int(input("Numero #2: "))
  

# def operacionAritmetica(num1,num2,opcion):  
#     if opcion=="1" or opcion=="+" or opcion=="SUMA":
#       return f"{n1}+{n2}={n1+n2}"
#     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
#      return f"{n1}-{n2}={n1-n2}"
#     elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
#      return f"{n1}*{n2}={n1*n2}"
#     elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
#      return f"{n1}/{n2}={n1/n2}"  
    
# def esperarTecla():
#   print("Oprima cualquier tecla para continuar ...")
#   input()

opcion=True 
   
while opcion:
 os.system("clear")
 print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- SALIR ")
 opcion=input("\t Elige una opción: ").upper()
 
 if opcion!="5":
  n1,n2=solicitarNumeros()
  print(operacionAritmetica(n1,n2,opcion))
  esperarTecla()
 else:  
     opcion=False    
     print("Terminaste la ejecucion del SW")