import os

salir = "no"

while(salir == "no"):
    os.system("clear")
    print("=========== CONVERSOR DE MONEDA ===========")
    cantidad = int(input("Ingrese la cantidad de conversiones que va a realizar: "))

    for veces in range(cantidad):
        print("\n================ OPCIONES ================")
        print("1. Dólares a Soles\n" \
            "2. Soles a Dólares\n" \
            "==========================================\n")
        
        cambio = 3
        
        opcion = int(input("Ingrese la conversión que desee realizar: "))

        if opcion == 1:
            dolares = float(input("Ingrese el monto en dólares($): "))
            conversion = dolares * cambio
            print(f"\nRESULTADO: $ {dolares} son S/. {conversion}\n")
        elif opcion == 2:
            soles = float(input("Ingrese el monto en soles(S/.): "))
            conversion = soles / cambio
            print(f"\nRESULTADO: S/. {soles} son $ {conversion}\n")
        else:
            print("ERROR: Debe ingresar una de las opciones válidas (1 o 2)")
        
    salir = input("Desea salir? (si/no) ")
    if salir.lower() == "si":
        break