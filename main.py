from AsistenteAcademico import modo_ia_simulada
from student import Student

from tareas import mostrar_tareas, sugerencia_ayuda
import datetime
import tkinter as tk
from tkinter import messagebox
from DatosRandom import dato_curioso_random

# Simulamos el inicio
import sqlite3
import random

DB_NAME = "asistente_estudio.db"

def obtener_estudiante_random():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT nombre, carrera FROM estudiantes")
    todos = cursor.fetchall()

    estudiante = random.choice(todos)

    conn.close()
    return estudiante  # devuelve (nombre, carrera)


nombre, carrera = obtener_estudiante_random()
dato = dato_curioso_random()

# Funciones de los botones
def mostrar_tareas():
    hoy = datetime.date.today().isoformat()
    conn = sqlite3.connect("asistente_estudio.db")
    cursor = conn.cursor()
    cursor.execute("SELECT materia, descripcion, fecha FROM tareas WHERE fecha = ?", (hoy,))
    tareas = cursor.fetchall()
    conn.close()

    tareas_win = tk.Toplevel(root)
    tareas_win.title("📋 Tareas de Hoy")

    if tareas:
        for tarea in tareas:
            tk.Label(tareas_win, text=f"- {tarea[0]}: {tarea[1]} (Fecha: {tarea[2]})").pack(anchor="w", padx=10, pady=2)
    else:
        tk.Label(tareas_win, text="No hay tareas registradas para hoy.").pack(padx=10, pady=10)

def pedir_ayuda():
    ayuda_win = tk.Toplevel(root)
    ayuda_win.title("Pedir Ayuda")
    tk.Label(ayuda_win, text="¿Sobre qué materia necesitas ayuda?").pack(pady=5)

    entry_materia = tk.Entry(ayuda_win)
    entry_materia.pack(pady=5)

    def buscar_ayuda():
        materia = entry_materia.get().lower()
        ayuda = {
            "logica": "Te recomiendo leer 'Cómo resolverlo' de Polya o ver ejercicios en YouTube.",
            "matematicas": "Puedes repasar en Khan Academy o buscar ejercicios en Geogebra.",
        }
        if materia not in ayuda:
            modo_ia_simulada(materia)
        else:
            messagebox.showinfo("🔍 Ayuda", ayuda[materia])
        ayuda_win.destroy()  # Cerramos la ventana de ayuda luego de mostrarla

    tk.Button(ayuda_win, text="Buscar", command=buscar_ayuda).pack(pady=5)

# Crear ventana principal
root = tk.Tk()
root.title("Asistente de Estudio")
root.geometry("800x480")

# Encabezado
tk.Label(root, text=f"Bienvenido {nombre}, {carrera}", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text=f"Dato curioso del día:\n📚 {dato}", wraplength=400, justify="left").pack(pady=10)

# Botones
tk.Button(root, text="📚 Ver tareas", command=mostrar_tareas, width=20).pack(pady=5)
tk.Button(root, text="❓ Pedir ayuda", command=pedir_ayuda, width=20).pack(pady=5)
tk.Button(root, text="🚪 Salir", command=root.quit, width=20).pack(pady=5)

root.mainloop()
