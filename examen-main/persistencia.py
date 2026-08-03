import json
import os 


ARCHIVO = "evaluaciones.json"

def cargar_datos():
    if not os. path.exists(ARCHIVO):
        with open(ARCHIVO, "w") as archivo:
            json.dump([], archivo)
    
    with open(ARCHIVO, "r") as archivo:
        return json.load(archivo)

def guardar_datos_(datos):
    with open(ARCHIVO,"w") as archivo:
        json.dump(datos, archivo, indent=4)
    
