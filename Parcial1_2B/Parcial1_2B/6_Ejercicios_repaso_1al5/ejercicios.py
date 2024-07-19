

# Solicitar al usuario que ingrese dos números
num1 = int(input("Ingrese el primer número: "))
num2= int(input("Ingrese el segundo número: "))


if num1 < num2:
    print("Los números entre ", num1, " y ", num2, " son: ")
    for cont in range(num1 + 1, num2 + 1):
        print(cont)
else:
        print("Coloca un valor inicial menor al segundo")