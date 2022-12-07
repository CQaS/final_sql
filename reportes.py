import os
from base import buscarActivos, buscarDesocupados, buscarProfesion, buscarRango
from tryExcept import tryExceptOptions, matchLetras


def trabajadorActivo():
    os.system("cls")
    print("Mostrar trabajadores Activos")
    datos = buscarActivos()
    for line in datos:
        print(f'''
            DNI: {line[1]}
            Nombre: {line[2]}
            Edad: {line[3]}
            Profesion: {line[4]}
            ''')


def trabajadorDesocupados():
    os.system("cls")
    print("Mostrar trabajadores Desocupados")
    datos = buscarDesocupados()
    for line in datos:
        print(f'''
            DNI: {line[1]}
            Nombre: {line[2]}
            Edad: {line[3]}
            Profesion: {line[4]}
            ''')


def trabajadorRangoEdad():
    os.system("cls")
    print("Mostrar Desocupados en un rango de edad")
    edadMinima = tryExceptOptions("Edad minima: ")
    edadMaxima = tryExceptOptions("Edad maxima: ")
    datos = buscarRango(edadMinima, edadMaxima)
    for line in datos:
        print(f'''
            DNI: {line[1]}
            Nombre: {line[2]}
            Edad: {line[3]}
            Profesion: {line[4]}
            ''')


def trabajadorProfesion():
    os.system("cls")
    print("Mostrar trabajadores según su Profesión")
    profesion = matchLetras("Profesion: ")
    datos = buscarProfesion(profesion)
    for line in datos:
        print(f'''
            DNI: {line[1]}
            Nombre: {line[2]}
            Edad: {line[3]}
            Profesion: {line[4]}
            ''')
