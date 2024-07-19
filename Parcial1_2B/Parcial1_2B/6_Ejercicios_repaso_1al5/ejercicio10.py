#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron
reprobado=0
aprobado=0
alu=1
for i in range (1, 16):
    cali=float(input(f"Coloca la calificacion de tu alumno No: {alu}.- es:"))
    alu+=1
    if cali >=8:
        aprobado+=1 #hola 
    else:
        reprobado +=1

print(f"Los aprobados son {aprobado} y los reprobados son {reprobado}")
