#Entrada
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

operacion = input("Ingrese la operación a realizar(+,-,x,/): ")

resultado = 0

#Proceso
if operacion == "+":
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
elif operacion == "x":
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
elif operacion == "/":
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")
else:
    print("ERROR: Debe ingresar una operación válida(+/-)")
    exit()

