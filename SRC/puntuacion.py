# -*- coding: utf-8 -*-

def traerMaximaPuntuacion():
    
    maximaPuntuacion = 0
    
    try:
        archivo_puntuacion_mas_alta = open("puntuacion.txt", "r")
        maximaPuntuacion = int(archivo_puntuacion_mas_alta.read())
        archivo_puntuacion_mas_alta.close()
        #print("La puntuacion mas alta es", maximaPuntuacion)
    except IOError:
        print("Aun no existe una puntuacion mas alta.")
    except ValueError:
        print("No se puede leer la puntuacion.")
 
    return maximaPuntuacion
 
def actualizarMaximaPuntuacion(nuevaMaximaPuntuacion):
    try:
        archivo_puntuacion_mas_alta = open("puntuacion.txt", "w")
        archivo_puntuacion_mas_alta.write(str(nuevaMaximaPuntuacion))
        archivo_puntuacion_mas_alta.close()
    except IOError:
        print("No se puede guardar la puntuacion.")