
from gestionar import altaTrabajador, modificarTrabajador, eliminarTrabajador, status
from tryExcept import tryExceptOptions
import os
from reportes import trabajadorActivo, trabajadorDesocupados, trabajadorRangoEdad, trabajadorProfesion
from decoraciones import decorar, info
from base import createTabla
createTabla()


while True:
    os.system("cls")
    print("""
        ┌──────────────────────────┐
        │ TRABAJO PRACTICO GRUPO A │
        │   CONSULTORA DE TRABAJO  │
        │   CURSO CODO A CODO 4.0  │
        └──────────────────────────┘\n
        ┌──────────────────────────┐
        │     Menú Principal       │ 
        └──────────────────────────┘\n                   
       ┌───────────────────────────────────┐
       │ [1] Gestion de trabajadores       │
       │ [2] Reportes                      │
       │ [3] Cambiar status del trabajador │
       │ [4] Salir                         │
       └───────────────────────────────────┘
    """)

    opcion = tryExceptOptions()
    if opcion == 4:
        break

    elif opcion == 1:
        os.system("cls")
        while True:
            print("""
                ┌───────────────────────────────────┐
                │     Gestion de trabajadores       │
                └───────────────────────────────────┘\n
                ┌──────────────────────────────────────┐
                │ [1] Ingresar nuevo trabajador        │
                │ [2] Modificar datos de un trabajador │
                │ [3] Eliminar trabajador              │
                │ [4] Volver al Menu Principal         │
                └──────────────────────────────────────┘
                """)
        
            opcion = tryExceptOptions()
            if opcion == 4:
                break

            elif opcion == 1:
                altaTrabajador()
                decorar()
                os.system("pause")
            
            elif opcion == 2:
                decorar()
                modificarTrabajador()
                os.system("pause")
            
            elif opcion == 3:
                #dni = tryExceptOptions("Ingrese DNI del trabajador que quiere eliminar: ")
                decorar()
                eliminarTrabajador() 
                os.system("pause")

    elif opcion == 2:
        os.system("cls")
        while True:
            
            info('REPORTES')
                
            print("""
                ┌──────────────────────────────────────────────┐
                │  [1] Mostrar trabajadores Activos            │
                │  [2] Mostrar trabajadores Desocupados        │
                │  [3] Mostrar Desocupados en un rango de edad │
                │  [4] Mostrar trabajadores segun su Profesion │
                │  [5] Volver al Menu Principal                │
                └──────────────────────────────────────────────┘\n
                """)
            opcion = tryExceptOptions()
            if opcion == 5:
                break

            elif opcion == 1:
                decorar()
                trabajadorActivo()
                os.system("pause")

            elif opcion == 2:
                decorar()
                trabajadorDesocupados()
                os.system("pause")

            elif opcion == 3:
                decorar()
                trabajadorRangoEdad()
                os.system("pause")

            elif opcion == 4:
                decorar()
                trabajadorProfesion()
                os.system("pause")

    elif opcion == 3:
        decorar()
        status()
        print("El Status fue actualizado")
        os.system("pause")

os.system("cls")
print("""
     ┌─────────────────────────┐
     │    Fin del Programa     │
     └─────────────────────────┘\n
    """)
