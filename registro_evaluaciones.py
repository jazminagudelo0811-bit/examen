from persistencia import cargar_datos , guardar_datos_

def registrar_evaluacion():
    datos = cargar_datos():
        
        estudiante = input("nombre del estudiante: ")
        intructor = input ("nombre del instructor: ")
        fecha = input( "fecha (dd/mm/aa): ")
        
        while true :
            try :
                calificacion = float(input("calificacion (0-100): "))
                if 0 <= calificacion <= 100:
                else:
                    print("la calificacion debe estar entre 0 y 100. ")
            except:
                print("ingrese un numero valido. ") 
                
                       from persistencia import cargar_datos, guardar_datos

def registrar_evaluacion():
    datos = cargar_datos()

    estudiante = input("Nombre del estudiante: ")
    instructor = input("Nombre del instructor: ")
    fecha = input("Fecha (dd/mm/aaaa): ")

    while True:
        try:
            calificacion = float(input("Calificación (0-100): "))
            if 0 <= calificacion <= 100:
                break
            else:
                print("La calificación debe estar entre 0 y 100.")
        except:
            print("Ingrese un número válido.")

    evaluacion = {
        "estudiante": estudiante,
        "instructor": instructor,
        "fecha": fecha,
        "calificacion": calificacion
    }

    datos.append(evaluacion)
    guardar_datos(datos)

    print("Evaluación registrada correctamente.")

def consultar_estudiante():
    datos = cargar_datos()

    nombre = input("Nombre del estudiante: ")

    encontrado = False

    for eva in datos:
        if eva["estudiante"].lower() == nombre.lower():
            print("--------------------------")
            print("Estudiante:", eva["estudiante"])
            print("Instructor:", eva["instructor"])
            print("Fecha:", eva["fecha"])
            print("Calificación:", eva["calificacion"])
            encontrado = True

    if not encontrado:
        print("No existen registros para ese estudiante.")

def calcular_promedio():
    datos = cargar_datos()

    if len(datos) == 0:
        print("No hay datos suficientes.")
        return

    suma = 0

    for eva in datos:
        suma += eva["calificacion"]

    promedio = suma / len(datos)

    print("Promedio general:", round(promedio, 2))