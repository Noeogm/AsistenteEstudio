# crear base de datos predefinidas
import sqlite3

DB_NAME = "asistente_estudio.db"

def crear_y_poblar_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Crear tabla estudiantes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            carrera TEXT NOT NULL
        )
    """)

    # Crear tabla tareas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            materia TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            fecha TEXT NOT NULL
        )
    """)

    # Insertar estudiantes solo si la tabla está vacía
    cursor.execute("SELECT COUNT(*) FROM estudiantes")
    if cursor.fetchone()[0] == 0:
        estudiantes = [
            ("Ana", "Ingeniería"), ("Luis", "Medicina"), ("Carlos", "Derecho"),
            ("María", "Psicología"), ("Jorge", "Arquitectura"), ("Lucía", "Economía"),
            ("Pedro", "Matemáticas"), ("Elena", "Biología"), ("Raúl", "Física"),
            ("Camila", "Literatura"), ("Andrés", "Historia"), ("Valeria", "Química"),
            ("Tomás", "Computación"), ("Sofía", "Filosofía"), ("Gabriel", "Sociología"),
            ("Daniela", "Arte"), ("Mateo", "Diseño"), ("Fernanda", "Periodismo"),
            ("Iván", "Marketing"), ("Paula", "Finanzas")
        ]
        cursor.executemany("INSERT INTO estudiantes (nombre, carrera) VALUES (?, ?)", estudiantes)

    # Insertar tareas de prueba si la tabla está vacía
    # Insertar tareas de prueba si la tabla está vacía
    cursor.execute("SELECT COUNT(*) FROM tareas")
    if cursor.fetchone()[0] == 0:
        tareas = [
            ("Matemáticas", "Estudiar límites y derivadas", "2025-05-21"),
            ("Física", "Resolver problemas de cinemática", "2025-05-21"),
            ("Química", "Repasar tabla periódica y enlaces químicos", "2025-05-22"),
            ("Historia", "Leer sobre la Revolución Francesa", "2025-05-23"),
            ("Literatura", "Analizar poema de Pablo Neruda", "2025-05-23"),
            ("Lógica", "Practicar razonamiento deductivo", "2025-05-24"),
            ("Biología", "Estudiar mitosis y meiosis", "2025-05-24"),
            ("Informática", "Revisar estructuras de datos básicas", "2025-05-25"),
            ("Economía", "Leer sobre oferta y demanda", "2025-05-25"),
            ("Psicología", "Resumen sobre teorías del aprendizaje", "2025-05-26"),
            ("Filosofía", "Leer a Platón y Sócrates", "2025-05-26"),
            ("Arte", "Investigar sobre el Renacimiento italiano", "2025-05-27")
        ]
        cursor.executemany("INSERT INTO tareas (materia, descripcion, fecha) VALUES (?, ?, ?)", tareas)



    conn.commit()
    conn.close()

crear_y_poblar_db()
