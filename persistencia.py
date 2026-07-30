import json
import os 


ARCHIVO = "evaluaciones.json"

def cargar_datos():
    if not os. path.exists(ARCHIVO):
        while open(ARCHIVO, "w" ) as ARCHIVO:
            json.dum([], ARCHIVO)
    
    with open
    (ARCHIVO, "r" ) as ARCHIVO:
        return json.load(ARCHIVO)

def guardar_datos_(datos):
    with open(ARCHIVO,"w") as archivo:
        json.dump(datos, archivo, indent=4)
    
