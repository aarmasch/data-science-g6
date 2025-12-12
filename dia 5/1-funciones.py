def saludar(nombre):
    mensaje = f'Hola {nombre}'
    return mensaje

usuario = input('Hola ¿Cómo te llamas?: ')
print(saludar(usuario))