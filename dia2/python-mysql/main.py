import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='db_g6'
)

print("Connection established:", connection.is_connected())

cursor = connection.cursor()
cursor.execute("SELECT id, nombre, email from alumno;")
resultado = cursor.fetchall()
for registro in resultado:
    print(f"----- Registro {registro[0]} -----")
    print(f"Nombre: {registro[1]}")
    print(f"Email: {registro[2]}")

connection.close()

