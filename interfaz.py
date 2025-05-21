import sqlite3
import tkinter as tk
import random

DB_NAME = 'asistente_estudio.db'

def obtener_estudiante_random():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, carrera FROM estudiantes")
    estudiantes = cursor.fetchall()
    conn.close()
    return random.choice(estudiantes) if estudiantes else ("Sin datos", "Sin datos")

def actualizar_datos():
    nombre, carrera = obtener_estudiante_random()
    nombre_label.config(text=f"Nombre: {nombre}")
    carrera_label.config(text=f"Carrera: {carrera}")

# Crear ventana
ventana = tk.Tk()
ventana.title("Asistente de Estudio")
ventana.geometry("350x200")
ventana.resizable(False, False)

# Etiquetas
titulo_label = tk.Label(ventana, text="Bienvenido/a", font=("Arial", 16))
titulo_label.pack(pady=10)

nombre_label = tk.Label(ventana, text="", font=("Arial", 12))
nombre_label.pack(pady=5)

carrera_label = tk.Label(ventana, text="", font=("Arial", 12))
carrera_label.pack(pady=5)

# Botón para cambiar estudiante
boton_cambiar = tk.Button(ventana, text="Cambiar estudiante", command=actualizar_datos)
boton_cambiar.pack(pady=10)

# Mostrar primer estudiante
actualizar_datos()

# Ejecutar
ventana.mainloop()
