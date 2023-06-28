from tkinter import *
import tkinter as tk
from base import buscarActivos, buscarDesocupados, buscarProfesion, buscarRango
from tryExcept import tryExceptOptions, matchLetras


def reporte():
    ventanaReportes = tk.Toplevel()
    ventanaReportes.title('Reportes de trabajadores')
    ventanaReportes.geometry('500x300')
    ventanaReportes.configure(background='dark turquoise')
    e3 = tk.Label(ventanaReportes, text='''
                \n
                ┌──────────────────────────────────────┐
                     Seleccione una opcion del menu    
                └──────────────────────────────────────┘
                ''', bg='pink', fg='white')
    e3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
    btnActivos = tk.Button(ventanaReportes, text='Mostrar trabajadores Activos',
                           fg='blue', command=trabajadorActivo)
    btnActivos.pack(side=tk.TOP)
    btnDesocupados = tk.Button(ventanaReportes, text='Mostrar trabajadores Desocupados',
                               fg='blue', command=trabajadorDesocupados)
    btnDesocupados.pack(side=tk.TOP)
    btnEdad = tk.Button(ventanaReportes, text='Mostrar Desocupados en un rango de edad',
                        fg='blue', command=trabajadorRangoEdad)
    btnEdad.pack(side=tk.TOP)
    btnProfesion = tk.Button(ventanaReportes, text='Mostrar trabajadores segun su Profesion',
                             fg='blue', command=trabajadorProfesion)
    btnProfesion.pack(side=tk.TOP)
    btnSalir = tk.Button(ventanaReportes, text='Salir',
                         fg='blue', command=ventanaReportes.destroy)
    btnSalir.pack(side=tk.TOP)


def trabajadorActivo():
    ventanaActivos = tk.Toplevel()
    ventanaActivos.title('Trabajadores Activos ')
    ventanaActivos.geometry('600x500')
    ventanaActivos.configure(background='dark turquoise')
    etiqueta = tk.Label(ventanaActivos, text='''
                \n
                ┌──────────────────────────────────────┐
                    Lista de los Trabajadores Activos    
                └──────────────────────────────────────┘
                ''', bg='pink', fg='white')
    etiqueta.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    datos = buscarActivos()
    for line in datos:
        listar = tk.Label(ventanaActivos, text=f'''
            DNI: {line[1]}
            Nombre: {line[2]}
            Edad: {line[3]}
            Profesion: {line[4]}
            ''', bg='white', fg='blue')
        listar.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)


def trabajadorDesocupados():
    ventanaDesocupados = tk.Toplevel()
    ventanaDesocupados.title('Trabajadores Desocupados ')
    ventanaDesocupados.geometry('600x500')
    ventanaDesocupados.configure(background='dark turquoise')
    etiqueta = tk.Label(ventanaDesocupados, text='''
                    \n
                    ┌──────────────────────────────────────┐
                      Lista de los Trabajadores Desocupados    
                    └──────────────────────────────────────┘
                    ''', bg='pink', fg='white')
    etiqueta.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    datos = buscarDesocupados()
    for line in datos:
        listar = tk.Label(ventanaDesocupados, text=f'''
                DNI: {line[1]}
                Nombre: {line[2]}
                Edad: {line[3]}
                Profesion: {line[4]}
                ''', bg='white', fg='blue')
        listar.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)


def trabajadorRangoEdad():
    ventanaRango = tk.Toplevel()
    ventanaRango.title('Trabajadores por Rango de edad')
    ventanaRango.geometry('600x500')
    ventanaRango.configure(background='dark turquoise')
    etiqueta = tk.Label(ventanaRango, text='''
                    \n
                    ┌──────────────────────────────────────┐
                       Lista de los Trabajadores por edad    
                    └──────────────────────────────────────┘
                    ''', bg='pink', fg='white')
    etiqueta.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    lbledad1 = tk.Label(ventanaRango, text=f'Edad minima:',
                        bg='pink', fg='white')
    lbledad1.pack(padx=3, pady=3, ipadx=5, ipady=5, fill=tk.X)
    inputEdad1 = tk.Entry(ventanaRango)
    inputEdad1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    lbledad2 = tk.Label(ventanaRango, text=f'Edad maxima:',
                        bg='pink', fg='white')
    lbledad2.pack(padx=3, pady=3, ipadx=5, ipady=5, fill=tk.X)
    inputEdad2 = tk.Entry(ventanaRango)
    inputEdad2.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    btnBuscar = tk.Button(ventanaRango, text='Buscar',
                        command=lambda: buscarPorRango(inputEdad1, inputEdad2, ventanaRango))
    btnBuscar.pack(side=tk.TOP)

    btnSalir = tk.Button(ventanaRango, text='Cancelar',
                         command=ventanaRango.destroy)
    btnSalir.pack(side=tk.TOP)


def buscarPorRango(inputEdad1, inputEdad2, ventanaRango):
    edadMinima = tryExceptOptions(inputEdad1.get())
    edadMaxima = tryExceptOptions(inputEdad2.get())
    datos = buscarRango(edadMinima, edadMaxima)
    for line in datos:
        listar = tk.Label(ventanaRango, text=f'''
                DNI: {line[1]}
                Nombre: {line[2]}
                Edad: {line[3]}
                Profesion: {line[4]}
                ''', bg='white', fg='blue')
        listar.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)


def trabajadorProfesion():

    ventanaProfesion = tk.Toplevel()
    ventanaProfesion.title('Trabajadores por Profesion')
    ventanaProfesion.geometry('600x500')
    ventanaProfesion.configure(background='dark turquoise')
    etiqueta = tk.Label(ventanaProfesion, text='''
                        \n
                        ┌──────────────────────────────────────┐
                           Lista de Trabajadores por profesion    
                        └──────────────────────────────────────┘
                        ''', bg='pink', fg='white')
    etiqueta.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    lblprofesion = tk.Label(ventanaProfesion, text=f'Profesion:',
                        bg='pink', fg='white')
    lblprofesion.pack(padx=3, pady=3, ipadx=5, ipady=5, fill=tk.X)
    inputProfesion = tk.Entry(ventanaProfesion)
    inputProfesion.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    btnBuscar = tk.Button(ventanaProfesion, text='Buscar',
                        command=lambda: buscarPorProfesion(inputProfesion, ventanaProfesion))
    btnBuscar.pack(side=tk.TOP)

    btnSalir = tk.Button(ventanaProfesion, text='Cancelar',
                        command=ventanaProfesion.destroy)
    btnSalir.pack(side=tk.TOP)


    def buscarPorProfesion(inputProfesion, ventanaProfesion):
        profesion = matchLetras(inputProfesion.get())
        datos = buscarProfesion(profesion)
        for line in datos:
            listar = tk.Label(ventanaProfesion, text=f'''
                    DNI: {line[1]}
                    Nombre: {line[2]}
                    Edad: {line[3]}
                    Profesion: {line[4]}
                    ''', bg='white', fg='blue')
            listar.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
