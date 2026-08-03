from registro_evaluaciones import registrar_evaluacion,consultar_estudiante,calcular_promedio

while True:

    print("\n========== DRIVE SAFE ==========")
    print("1. Registrar evaluación")
    print("2. Consultar estudiante")
    print("3. Calcular promedio general")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_evaluacion()

    elif opcion == "2":
        consultar_estudiante()

    elif opcion == "3":
        calcular_promedio()

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
    



