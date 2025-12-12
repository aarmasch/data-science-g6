dias = ["Lunes","Martes","Miercoles","Jueves","Viernes"]

print(dias[0])

#Agregar elementos
dias.append("Sábado")
dias.append("Domingo")

#Eliminar elementos
#Primera manera
dias.pop(2)
#Segunda manera
del dias[0:2]

# actualizar un valor de la lista
dias[-1] = "Lunes"

for dia in dias:
    print(dia)

