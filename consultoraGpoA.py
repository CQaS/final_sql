import tkinter as tk
from gestionar import status, gestion
from reportes import reporte
from base import createTabla
createTabla()

ventanaPrincipal = tk.Tk()
ventanaPrincipal.title('Menú Principal')
ventanaPrincipal.geometry('500x300')
ventanaPrincipal.configure(background='grey')

titulo = tk.Label(ventanaPrincipal, text='''
        ┌──────────────────────────┐
          TRABAJO PRACTICO GRUPO A  
            CONSULTORA DE TRABAJO   
            CURSO CODO A CODO 4.0   
        └──────────────────────────┘
    ''', bg='white', fg='black')
titulo.pack(padx=5, pady=5, ipadx=5, ipady=5)
btnGestion = tk.Button(ventanaPrincipal, text='Gestion de trabajadores',
                       fg='blue', command=gestion)
btnGestion.pack(side=tk.TOP)
btnReportes = tk.Button(ventanaPrincipal, text='Reportes',
                        fg='blue', command=reporte)
btnReportes.pack(side=tk.TOP)
btnStatus = tk.Button(ventanaPrincipal, text='Cambiar status del trabajador',
                      fg='blue', command=status)
btnStatus.pack(side=tk.TOP)
btnSalir = tk.Button(ventanaPrincipal, text='Salir',
                     fg='blue', command=ventanaPrincipal.destroy)
btnSalir.pack(side=tk.TOP)

ventanaPrincipal.mainloop()
