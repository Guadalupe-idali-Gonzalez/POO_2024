#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario
impar=0
tipo=""
n1=int(input("Ingrese el primer numero (inicio del rango): "))
n2=int(input("Ingrese el segundo numero: (fin del rango): "))

for i in range(n1+1,n2):
    impar=i%2
   
    if impar > .1:
        print(i)
35