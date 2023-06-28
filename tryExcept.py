import re
import tkinter as tk
from tkinter import messagebox

def tryExceptOptions(ingreso):    
        try:
            opcion = int(ingreso)
            return opcion
        except ValueError:
            messagebox.showwarning('ALERTA', 'Ingresa solo numeros!') 


def matchLetras(ingreso):
        # solo letras
        if re.match("^[A-Za-z áéíóúÁÉÍÓÚñÑ]*$", ingreso):
            return ingreso
        else:
            messagebox.showwarning('ALERTA', 'Ingresa solo letras!')