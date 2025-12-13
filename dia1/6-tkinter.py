from tkinter import *
from tkinter import messagebox

def saludar():
    nombre = txt_nombre.get()
    print(f"Hola, {nombre}!")
    messagebox.showinfo("Saludo", f"Hola, {nombre}!")

#Creamos un objeto de la clase Tk
app = Tk()

#Título de la ventana
app.title("Mi primera app con Tkinter")

#Dimensiones de la ventana
app.geometry("300x100")

#Creamos un objeto frame
frame = Frame(app)
frame.grid(row=0,column=0,padx=20,pady=10)

#crear una etiqueta (label) dentro del frame
lb_nombre = Label(frame,text="Nombre :")
lb_nombre.grid(row=0,column=0)
#crear una caja de texto (entry) dentro del frame
txt_nombre = Entry(frame)
txt_nombre.grid(row=0,column=1)
#crear un botón (button) dentro del frame
btn_saludar = Button(frame,text="Saludar",command=saludar)
btn_saludar.grid(row=0,column=3,padx=20,pady=20)

#Mostramos la ventana
app.mainloop()