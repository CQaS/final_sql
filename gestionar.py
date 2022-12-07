import os
from decoraciones import info
from base import insert, buscar, actualizar, eliminar, cambiarStatus
from tryExcept import tryExceptOptions, tryExceptNumero, matchLetras


def altaTrabajador():
    os.system("cls")
    print("Ingresar nuevo trabajador")
    dni = tryExceptOptions("Ingrese DNI: ")
    nombre = matchLetras("Ingrese nombre: ")
    edad = tryExceptOptions("Ingrese la edad: ")
    profesion = matchLetras("Ingrese su profesión: ")

    activo = input("Actualmente, está trabajando? (s/n):")
    if activo == "s" or activo == "S":
        activo = 'True'
    else:
        activo = 'False'
    
    datos = buscar(dni)

    if datos == []:
        res = insert(dni, nombre, edad, profesion, activo)
        print(f'Informacion: {res}')
    else:
        info('DNI no Existe!')


def modificarTrabajador():
    os.system("cls")
    print("Modificar datos de un trabajador")

    while True:
        dni = tryExceptOptions("Ingrese DNI del trabajador a modificar: ")
        datos = buscar(dni)

        if datos !=  []:

            for line in datos:  #
                id = line[0]
                dni = line[1]
                nombre = line[2]
                edad = line[3]
                profesion = line[4]
                activo = line[5]

                nombreIngresado = matchLetras(
                    f"Modificar nombre de {line[2]}? \n Ingrese:  ")
                if nombreIngresado:
                    nombre = nombreIngresado

                edadIngresada = tryExceptNumero(
                    f"La edad del Trabajador es {line[3]}. Modificar? \n Ingrese: ")
                if edadIngresada:
                    edad = edadIngresada

                profesionIngresada = matchLetras(
                    f"La profesión del trabajador es {line[4]}. Modificar? \n Ingrese: ")
                if profesionIngresada:
                    profesion = profesionIngresada

                activoIngresado = input("Actualmente, está trabajando? (s/n): ")
                if activoIngresado == "s" or activoIngresado == "S":
                    activo = 'True'
                else:
                    activo = 'False'
                
                print(actualizar(id, dni, nombre, edad, profesion, activo))

            break
            
        else:
            info('DNI no encontrado!')    


def eliminarTrabajador():
    os.system("cls")
    print("Eliminar trabajador")
    dni = tryExceptOptions("Ingrese DNI del trabajador que quiere eliminar: ")
    
    datos = buscar(dni)

    if datos != []:
        print(eliminar(dni))
    else:
        info('DNI no encontrado!')


def status():
    os.system("cls")
    print(" Cambiar status del trabajador \n")
    dni = tryExceptOptions("Ingrese DNI del trabajador a modificar:")

    datos = buscar(dni)

    if datos != []:
        print(cambiarStatus(dni))
    else:
        info('DNI no encontrado!')
    
