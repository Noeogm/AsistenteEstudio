from student import Student
from DatosRandom import dato_curioso_random
from tareas import mostrar_tareas, sugerencia_ayuda
from datetime import date

# Simulamos el inicio
nombre = input("Bienvenido/a. ¿Cuál es tu nombre? ")
carrera = input("¿Qué carrera estudias? ")

usuario = Student(nombre, carrera)

# Simulamos materias y tareas registradas
usuario.agregar_materia("Matemáticas I")
usuario.agregar_materia("Introducción a la IA")

usuario.agregar_tarea({
    "materia": "Matemáticas I",
    "descripcion": "Resolver ejercicios de derivadas",
    "fecha": date.today().isoformat()
})

usuario.agregar_tarea({
    "materia": "Introducción a la IA",
    "descripcion": "Leer el capítulo 2 del libro",
    "fecha": date.today().isoformat()
})

# Saludo inicial
print(f"\nHola {usuario.nombre} 👋")
print("Dato curioso del día:")
print("📚 Dato del día:", dato_curioso_random())
print("")

# Comandos básicos
while True:
    comando = input("\n¿Qué deseas hacer? (tareas / ayuda / salir): ").lower()

    if comando == "tareas":
        tareas = usuario.tareas_proximos_dias()
        mostrar_tareas(tareas)
    elif comando == "ayuda":
        tarea = input("¿Sobre qué materia necesitas ayuda? ")
        sugerencia_ayuda({"materia": tarea})
    elif comando == "salir":
        print("Hasta luego! 👋")
        break
    else:
        print("Comando no reconocido.")
