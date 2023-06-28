from base import insert, buscar, actualizar, eliminar, cambiarStatus
from tryExcept import tryExceptOptions, matchLetras
import tkinter as tk
from tkinter import messagebox


def invisible(widget):
    widget.pack_forget()


def visible(widget):
    widget.pack()


def gestion():
    ventanaGestion = tk.Toplevel()
    ventanaGestion.title('Gestion de trabajadores')
    ventanaGestion.geometry('500x300')
    ventanaGestion.configure(background='dark turquoise')
    etiqueta = tk.Label(ventanaGestion, text='''
                \n
                ┌──────────────────────────────────────┐
                     Seleccione una opcion del menu    
                └──────────────────────────────────────┘
                ''', bg='pink', fg='white')
    etiqueta.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)
    btnNuevo = tk.Button(ventanaGestion, text='Ingresar nuevo trabajador',
                         fg='blue', command=altaTrabajadores)
    btnNuevo.pack(side=tk.TOP)
    btnModificar = tk.Button(ventanaGestion, text='Modificar datos de un trabajador',
                             fg='blue', command=modificarTrabajadores)
    btnModificar.pack(side=tk.TOP)
    btnEliminar = tk.Button(ventanaGestion, text='Eliminar trabajador',
                            fg='blue', command=eliminarTrabajador)
    btnEliminar.pack(side=tk.TOP)
    btnSalir = tk.Button(ventanaGestion, text='Salir',
                         fg='blue', command=ventanaGestion.destroy)
    btnSalir.pack(side=tk.TOP)


def altaTrabajadores():
    ventanaAlta = tk.Toplevel()
    ventanaAlta.title('Alta de Trabajadores')
    ventanaAlta.geometry('800x500')
    ventanaAlta.configure(background='dark turquoise')

    lbldni = tk.Label(ventanaAlta, text='DNI', bg='pink', fg='white')
    lbldni.pack(padx=3, pady=3, ipadx=5, ipady=5, fill=tk.X)
    inputDni = tk.Entry(ventanaAlta)
    inputDni.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    lblnombre = tk.Label(ventanaAlta, text='Nombre', bg='pink', fg='white')
    lblnombre.pack(padx=3, pady=3, ipadx=5, ipady=5, fill=tk.X)
    inputNombre = tk.Entry(ventanaAlta)
    inputNombre.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    lbledad = tk.Label(ventanaAlta, text='Edad', bg='pink', fg='white')
    lbledad.pack(padx=3, pady=3, ipadx=5, ipady=5, fill=tk.X)
    inputEdad = tk.Entry(ventanaAlta)
    inputEdad.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    lblprofesion = tk.Label(
        ventanaAlta, text='Profesion', bg='pink', fg='white')
    lblprofesion.pack(padx=3, pady=3, ipadx=5, ipady=5, fill=tk.X)
    inputProfesion = tk.Entry(ventanaAlta)
    inputProfesion.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    lblactivo = tk.Label(ventanaAlta, text='Activo', bg='pink', fg='white')
    lblactivo.pack(padx=3, pady=3, ipadx=5, ipady=5, fill=tk.X)
    inputActivo = tk.Entry(ventanaAlta)
    inputActivo.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    btnAlta = tk.Button(ventanaAlta, text='Dar de alta',
                        command=lambda: altaTrabajador(inputDni, inputNombre, inputEdad, inputProfesion, inputActivo, ventanaAlta))
    btnAlta.pack(side=tk.TOP)
    btnSalir = tk.Button(ventanaAlta, text='Cancelar',
                         command=ventanaAlta.destroy)
    btnSalir.pack(side=tk.TOP)


def altaTrabajador(inputDni, inputNombre, inputEdad, inputProfesion, inputActivo, ventanaAlta):

    dni = tryExceptOptions(inputDni.get())
    nombre = matchLetras(inputNombre.get())
    edad = tryExceptOptions(inputEdad.get())
    profesion = matchLetras(inputProfesion.get())
    activo = matchLetras(inputActivo.get())

    if activo == "s" or activo == "S":
        activo = 'True'
    else:
        activo = 'False'

    datos = buscar(dni)

    if datos == []:
        res = insert(dni, nombre, edad, profesion, activo)
        messagebox.showwarning('INFO', res)
        ventanaAlta.withdraw()
    else:
        messagebox.showwarning('ALERTA', 'DNI ya existe')


def modificarTrabajadores():
    ventanaModificar = tk.Toplevel()
    ventanaModificar.title('Modificar datos de un Trabajador')
    ventanaModificar.geometry('800x500')
    ventanaModificar.configure(background='dark turquoise')

    lbldni = tk.Label(ventanaModificar, text='DNI a buscar',
                      bg='pink', fg='white')
    lbldni.pack(padx=3, pady=3, ipadx=5, ipady=5, fill=tk.X)

    inputDni = tk.Entry(ventanaModificar)
    inputDni.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    btnAlta = tk.Button(ventanaModificar, text='Buscar DNI',
                        command=lambda: modificacion(inputDni, ventanaModificar))
    btnAlta.pack(side=tk.TOP)

    btnSalir = tk.Button(ventanaModificar, text='Cancelar',
                         command=ventanaModificar.destroy)
    btnSalir.pack(side=tk.TOP)


def modificacion(inputDni, ventanaModificar):

    dni = tryExceptOptions(inputDni.get())
    datos = buscar(dni)

    if datos != []:

        for line in datos:  #
            id = line[0]
            dni = line[1]
            nombre = line[2]
            edad = line[3]
            profesion = line[4]
            activo = line[5]

            lbldni = tk.Label(ventanaModificar, text=f'DNI: {dni}',
                              bg='pink', fg='white')
            lbldni.pack(padx=3, pady=3, ipadx=5, ipady=5, fill=tk.X)

            lblnombre = tk.Label(
                ventanaModificar, text=f'Nombre: {nombre}', bg='pink', fg='white')
            lblnombre.pack(padx=3, pady=3, ipadx=5, ipady=5, fill=tk.X)
            inputNombre = tk.Entry(ventanaModificar)
            inputNombre.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

            lbledad = tk.Label(ventanaModificar, text=f'Edad: {edad}',
                               bg='pink', fg='white')
            lbledad.pack(padx=3, pady=3, ipadx=5, ipady=5, fill=tk.X)
            inputEdad = tk.Entry(ventanaModificar)
            inputEdad.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

            lblprofesion = tk.Label(
                ventanaModificar, text=f'Profesion: {profesion}', bg='pink', fg='white')
            lblprofesion.pack(padx=3, pady=3, ipadx=5, ipady=5, fill=tk.X)
            inputProfesion = tk.Entry(ventanaModificar)
            inputProfesion.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

            lblactivo = tk.Label(
                ventanaModificar, text=f'Activo: {activo}', bg='pink', fg='white')
            lblactivo.pack(padx=3, pady=3, ipadx=5, ipady=5, fill=tk.X)
            inputActivo = tk.Entry(ventanaModificar)
            inputActivo.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

            btnAlta = tk.Button(ventanaModificar, text='Modificar',
                                command=lambda: modificarTrabajador(id, inputDni, inputNombre, inputEdad, inputProfesion, inputActivo, ventanaModificar))
            btnAlta.pack(side=tk.TOP)

            btnSalir = tk.Button(ventanaModificar, text='Cancelar',
                                 command=ventanaModificar.destroy)
            btnSalir.pack(side=tk.TOP)

    else:
        messagebox.showwarning('ALERTA', 'DNI no existe')


def modificarTrabajador(id, inputDni, inputNombre, inputEdad, inputProfesion, inputActivo, ventanaModificar):

    dni = tryExceptOptions(inputDni.get())
    nombre = matchLetras(inputNombre.get())
    edad = tryExceptOptions(inputEdad.get())
    profesion = matchLetras(inputProfesion.get())
    activo = matchLetras(inputActivo.get())

    if activo == "s" or activo == "S":
        activo = 'True'
    else:
        activo = 'False'

    res = actualizar(id, dni, nombre, edad, profesion, activo)
    messagebox.showwarning('INFO', res)
    ventanaModificar.withdraw()


def eliminarTrabajador():
    ventanaEliminar = tk.Toplevel()
    ventanaEliminar.title('Eliminar datos de un Trabajador')
    ventanaEliminar.geometry('800x500')
    ventanaEliminar.configure(background='dark turquoise')

    lbldni = tk.Label(ventanaEliminar, text='DNI a buscar',
                      bg='pink', fg='white')
    lbldni.pack(padx=3, pady=3, ipadx=5, ipady=5, fill=tk.X)

    inputDni = tk.Entry(ventanaEliminar)
    inputDni.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    btnAlta = tk.Button(ventanaEliminar, text='Buscar DNI',
                        command=lambda: eliminacion(inputDni, ventanaEliminar))
    btnAlta.pack(side=tk.TOP)

    btnSalir = tk.Button(ventanaEliminar, text='Cancelar',
                         command=ventanaEliminar.destroy)
    btnSalir.pack(side=tk.TOP)


def eliminacion(inputDni, ventanaEliminar):

    dni = tryExceptOptions(inputDni.get())
    datos = buscar(dni)

    if datos != []:
        res = eliminar(dni)
        messagebox.showwarning('INFO', res)
        ventanaEliminar.withdraw()
    else:
        messagebox.showwarning('ALERTA', 'DNI no existe')


def status():
    ventanaStatus = tk.Toplevel()
    ventanaStatus.title('Cambiar Status de un Trabajador')
    ventanaStatus.geometry('800x500')
    ventanaStatus.configure(background='dark turquoise')

    lbldni = tk.Label(ventanaStatus, text='DNI a buscar',
                      bg='pink', fg='white')
    lbldni.pack(padx=3, pady=3, ipadx=5, ipady=5, fill=tk.X)

    inputDni = tk.Entry(ventanaStatus)
    inputDni.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

    btnAlta = tk.Button(ventanaStatus, text='Buscar DNI',
                        command=lambda: statusDe(inputDni, ventanaStatus))
    btnAlta.pack(side=tk.TOP)

    btnSalir = tk.Button(ventanaStatus, text='Cancelar',
                         command=ventanaStatus.destroy)
    btnSalir.pack(side=tk.TOP)


def statusDe(inputDni, ventanaStatus):

    dni = tryExceptOptions(inputDni.get())
    datos = buscar(dni)

    if datos != []:
        status = ''
        for line in datos:
            if line[5] == 'True':
                status = 'False'
            else:
                status = 'True'
            res = cambiarStatus(dni, status)
            messagebox.showwarning('INFO', res)
            ventanaStatus.withdraw()
    else:
        messagebox.showwarning('ALERTA', 'DNI no existe')
