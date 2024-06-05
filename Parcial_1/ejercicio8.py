#Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?
total=0
print ("Calcular x porcentaje de y numero")
num=float(input("Ingrese el numero: "))
porce=float(input("Ingrese el porcentaje: "))

total=num*(porce/100)
print(f"EL {porce}% de {num} es: {total}")