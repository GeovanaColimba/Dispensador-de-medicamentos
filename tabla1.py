import tkinter as tk
from tkinter import ttk
import pyrebase
import threading

# Configuración de Firebase
config = {
    "apiKey": "AIzaSyC4g_kyof0tw_eq8kUBlqLF3rOS-xQxGPg",
    "authDomain": "registro-alarmas.firebaseapp.com",
    "databaseURL": "https://registro-alarmas-default-rtdb.firebaseio.com",
    "projectId": "registro-alarmas",
    "storageBucket": "registro-alarmas.appspot.com",
    "messagingSenderId": "606369683568",
    "appId": ""
}

# Inicialización de la conexión a Firebase
firebase = pyrebase.initialize_app(config)

# Obtención de una referencia a la base de datos
db = firebase.database()

def actualizar_tabla():
    # Obtener datos de la base de datos (cambiar 'referencia_a_datos' por la referencia correcta)
    data = db.child("RegistroAlarmas/").get()
    dictionary = data.val()

    # Limpia los datos anteriores en la tabla
    for i in table.get_children():
        table.delete(i)

    # Insertar los nuevos datos en la tabla
    for index, compartimiento in enumerate(sorted(dictionary.keys())):
        compartimiento_data = dictionary[compartimiento]
        nomb = compartimiento_data.get("Medicamento", "")
        cant = compartimiento_data.get("cant", "")
        # Convierte la cantidad a entero (manteniendo la conversión)
        nomb = horario(nomb)
        cant = enteroCant(cant)
        compar = index + 1  # Agregar números del 1 al 6
        table.insert("", "end", values=(compar, nomb, cant))

    # Programar la próxima actualización en 60 segundos
    root.after(60000, actualizar_tabla)

# Función para convertir la cantidad a entero (manteniendo la conversión)
def enteroCant(valor):
    entero = valor.strip('"')
    if not entero.strip():
        return 0
    try:
        return int(entero)
    except ValueError:
        return 0

# Función para mantener la conversión de horario
def horario(valor):
    salida= valor.strip('"')
    return salida

# Crear la ventana de tkinter
root = tk.Tk()
root.title("Estado del dispensador")


# Tamaño de la ventana
ventana_ancho = 550
ventana_alto = 197

# Obtener el tamaño de la pantalla
pantalla_ancho = root.winfo_screenwidth()
pantalla_alto = root.winfo_screenheight()

# Calcular la posición de la ventana para que aparezca centrada al lado izquierdo
pos_x = (pantalla_ancho - ventana_ancho) // 2  # Ajusta este valor para cambiar la posición en el eje X
pos_y = (pantalla_alto - ventana_alto) // 2

# Establecer la posición de la ventana
root.geometry(f"{ventana_ancho}x{ventana_alto}+{pos_x}+{pos_y}")

style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 15))
style.configure("Treeview", font=("Arial", 15))

# Crear una tabla para mostrar los datos
table = ttk.Treeview(root, columns=("Compartimiento", "Medicamento", "Cantidad"), show="headings")


table.column("Compartimiento", width=150 ,anchor="center")
table.column("Medicamento", width=200, anchor="center")
table.column("Cantidad", width=160, anchor="center")

table.heading("Compartimiento", text="Compartimiento")
table.heading("Medicamento", text="Medicamento")
table.heading("Cantidad", text="Cantidad")
table.pack(pady=20)

# Llamar a la función para la primera actualización de la tabla
actualizar_tabla()

# Iniciar el bucle principal de tkinter
root.mainloop()
