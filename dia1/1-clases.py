class Automovil:
    def __init__(self, aa, pl, col, mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar

    def encender(self):
        print(f"Encendiendo el automovil {self.marca} con placa {self.placa} y de color {self.color} del año {self.año}.")
    
    def avanzar(self):
        print(f"El automovil {self.marca} está avanzando.")
    
    def acelerar(self):
        print(f"El automovil {self.marca} está acelerando.")
    
    def frenar(self):
        print(f"El automovil {self.marca} está frenando.")


vw = Automovil(1995, 'B8-0422', 'Amarillo', 'Volkswagen')
vw.encender()
vw.avanzar()
vw.acelerar()
vw.frenar()

tico = Automovil(2007, 'PT-5678', 'Rojo', 'Tico')
tico.encender()
tico.avanzar()
tico.acelerar()
tico.frenar()