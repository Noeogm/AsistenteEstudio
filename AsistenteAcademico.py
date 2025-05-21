def modo_ia_simulada(tema):
    print("🤖 Activando modo asistente académico inteligente...\n")

    explicaciones = {
        "álgebra": "Podés repasar los conceptos clave de álgebra como variables, ecuaciones lineales y factorización. Recomendación: YouTube - 'Álgebra desde cero'.",
        "lógica": "La lógica matemática se basa en proposiciones, operadores lógicos como AND, OR y tablas de verdad. Khan Academy tiene una buena sección.",
        "cálculo": "Recordá las reglas de derivación básicas y el concepto de límite. Muy útil repasar en el canal 'Blackpenredpen' de YouTube.",
        "trigonometría": "Es útil recordar identidades trigonométricas como seno²x + coseno²x = 1. Revisá ejercicios interactivos en Symbolab.",
        "física": "Repasá fórmulas como F = ma o E = mc². El canal 'Date un Vlog' tiene explicaciones geniales en español.",
        "historia": "Buscá líneas de tiempo o mapas mentales. El canal 'Academia Play' lo explica muy claro.",
    }

    respuesta = explicaciones.get(tema.lower(),
                                  f"No tengo aún una explicación específica para '{tema}', pero podés buscarlo en YouTube, Khan Academy o Wikipedia.")

    print(f"🧠 Explicación IA para '{tema}':\n{respuesta}")
    print("📌 Consejo: tomá nota y agregalo a tu agenda si es un tema que viene en examen.")
