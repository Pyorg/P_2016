# -*- coding: utf-8 -*-

def traerMaximaPuntuacion():
    
    maximaPuntuacion = 0
    
    try:
        archivo = open("puntuacion.txt", "r")
        filas = archivo.readlines()
        arrayPuntajes = []
        record = []
        for x in filas:
            arrayPuntajes.append(x)
        record = arrayPuntajes[0].split(" ");
        maximaPuntuacion = record[1]
        archivo.close()
    except IOError:
        print("Aun no existe una puntuacion mas alta.")
    except ValueError:
        print("No se puede leer la puntuacion.")
 
    return maximaPuntuacion

def traerMaximoJugador():
    
    maximoJugador = ""
    
    try:
        archivo = open("puntuacion.txt", "r")
        filas = archivo.readlines()
        arrayPuntajes = []
        record = []
        for x in filas:
            arrayPuntajes.append(x)
        record = arrayPuntajes[0].split(" ");
        maximoJugador = record[0]
        archivo.close()
    except IOError:
        print("Aun no existe una puntuacion mas alta.")
    except ValueError:
        print("No se puede leer la puntuacion.")
 
    return maximoJugador
 
def actualizarMaximaPuntuacion(nuevaMaximaPuntuacion, nombre):
    try:
        archivo = open("puntuacion.txt", "w")
        guardar = nombre + " " + str(nuevaMaximaPuntuacion)
        archivo.write(guardar)
        archivo.close()
    except IOError:
        print("No se puede guardar la puntuacion.")