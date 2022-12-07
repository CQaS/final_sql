import re

def tryExceptOptions(mensaje="Elija una opcion: "):
    while True:
        try:
            opcion = int(input(mensaje))
            return opcion
        except ValueError:
            print('\n\tALERTA: Ingresa un numero valido!\n')    


def tryExceptNumero(mensaje):
    opcion = ''
    while True:
        try:
            ingreso = input(mensaje)
            if ingreso:
                opcion = int(ingreso)
                return opcion
            else:
                return opcion
        except ValueError:
            print('\n\tALERTA: Ingresa un numero valido!\n')    


def matchLetras(mensaje):
    while True:
        nombre = input(mensaje)
        # solo letras
        if re.match("^[A-Za-z áéíóúÁÉÍÓÚñÑ]*$", nombre):
            return nombre
            break
        else:
            print('\n\tALERTA: Ingresa no valido!\n')
