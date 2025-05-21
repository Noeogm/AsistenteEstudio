from AsistenteAcademico import modo_ia_simulada
def mostrar_tareas(tareas):
    if not tareas:
        print("\n Analizando......\n")
        print("Bravo ! Al parecer No tienes tareas para hoy.")
        return
    print("Estas son tus tareas para hoy:")
    for t in tareas:
        print(f"- {t['materia']}: {t['descripcion']} (Fecha: {t['fecha']})")

def sugerencia_ayuda(tarea):
    materia = tarea["materia"].lower()
    if "mate" in materia:
        print("Puedes repasar en Khan Academy o buscar ejercicios en Geogebra.")
    elif "logica" in materia:
        print("Te recomiendo leer 'Cómo resolverlo' de Polya o ver ejercicios en YouTube.")
    else:
        print("🤖 Estoy buscando recursos útiles... 😉")
        usar_ia = input("¿Querés que active el modo asistente académico? (sí/no): ").strip().lower()

        if usar_ia in ["sí", "si", "s"]:
            modo_ia_simulada(materia)
        else:
            usar_internet = input(
                "¿Querés que busque información en internet sobre este tema? (sí/no): ").strip().lower()
            if usar_internet in ["sí", "si", "s"]:
                consulta = input("Decime exactamente qué querés que busque: ")
                print(f"🔎 Buscando en internet sobre: {consulta}")
                print("🌐 (Simulando búsqueda en internet...)")
                print(
                    f"👉 Encontré algo útil sobre '{consulta}': podés revisar este enlace o usar fuentes como Khan Academy, Wikipedia o YouTube.")
            else:
                print("👌 No hay problema. Si cambiás de idea, decime.")
