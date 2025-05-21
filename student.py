from datetime import datetime, timedelta
class Student:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera
        self.materias = []
        self.tareaspendientes = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def agregar_tarea(self, tarea):
        self.tareaspendientes.append(tarea)

    def tareas_proximos_dias(self, dias=10):
        hoy = datetime.today().date()
        limite = hoy + timedelta(days=dias)
        return [
            t for t in self.tareaspendientes
            if hoy <= datetime.strptime(t["fecha"], "%Y-%m-%d").date() <= limite
        ]