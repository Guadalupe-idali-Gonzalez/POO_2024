#Convertir los tipos de datos

#Nota: solo es posible en una concatenacion concatenar entre tipos de datos iguales

texto="Soy una cadena"
numero=23


print(texto+" soy una cadena2")
print(numero+34)


#Convertir un tipo de dato int a str
numero_str=str(numero)
print(texto+" "+numero_str) 
#Mas comun  para mostrar una cadena con un numero 
print(texto+ " "+str(numero))

#Convertir un str a int
n1=33
suma=int('23')+n1
print("suma: "+str(suma))

#Convertir un Float a INT
n1=33
n2=int(33.99)

suma=n1+n2
print(suma)

#Convertir de INT a Float

n1=3
n2=4

suma=n1+n2

print(f"La suma es: {float(suma)}")
print(f"La suma es: {suma}")
print("La suma es: "+ str(suma))