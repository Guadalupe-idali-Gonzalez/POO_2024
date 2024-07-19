#Hacer un programa que solicite numeros indefinidamente hasta que se introduzca el 111 y salir del programa

x = 0

while x != 111:
    x=float(input("coloca un numero"))
    print(x)
    if x == 111:
        print("Lista terminada")
        break