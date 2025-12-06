for i in range(1,10):
    print(i)
#TABLA DE MULTIPLICAR
tabla = int(input("Ingrese la tabla de multiplicar que desea ver: "))
for contador in range(1,13,1):
    resultado = tabla * contador
    print(f"{contador} x {tabla} = {resultado}")