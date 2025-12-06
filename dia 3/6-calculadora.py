import os
#CALCULADORA COMPLETA

salir = "no"
while(salir == "no"):
    os.system("clear")
    #ENTRADA
    print("========= CALCULADORA PYTHON =========")
    print("1. SUMA\n" \
    "2. RESTA\n" \
    "3. MULTIPLICAR\n" \
    "4. DIVIDIR\n" \
    "5. RAIZ CUADRADA\n" \
    "6. TABLA DE MULTIPLICAR")

    opcion = int(input("Ingrese la operación que desee realizar: "))

    if opcion == 5:
        import math
        numero = int(input("Ingrese el valor: "))
        resultado = math.sqrt(numero)
        print(f"La raiz cuadrada de {numero} es {resultado}")
    elif opcion == 6:
        tabla = int(input("Ingrese la tabla de multiplicar que desea ver: "))
        for contador in range(1,13,1):
            resultado = tabla * contador
            print(f"{contador} x {tabla} = {resultado}")
    elif opcion in range(1, 5):
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        if opcion == 1:
            operacion = "suma"
            resultado = num1 + num2
        elif opcion == 2:
            operacion = "resta"
            resultado = num1 - num2
        elif opcion == 3:
            operacion = "multiplicación"
            resultado = num1 * num2
        elif opcion == 4:
            operacion = "división"
            resultado = num1 / num2
        else:
            print("ERROR: Debe ingresar una operación válida(+/-)")
            exit()

        print(f"El resultado de la {operacion} es: {resultado}")
    else:
        print("ERROR: Debe elegir una opción válida")

    salir = input("Desea salir? (si/no) ")
    if salir == "si":
        break