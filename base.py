import sqlite3 as sql
from conexion import dbOpen


def createTabla():
    try:
        conn = dbOpen()
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS trabajadores (
                id integer PRIMARY KEY,
                dni integer,
                nombre text,
                edad integer,
                profesion text,
                activo text
            )
            """
        )
        conn.commit()
        conn.close()

    except sql.OperationalError as error:
        print("Error: ", error)


def insert(dni, nombre, edad, profesion, activo):
    try:
        conn = dbOpen()
        cursor = conn.cursor()
        query = f"INSERT INTO trabajadores (dni, nombre, edad, profesion, activo) VALUES ({dni},'{nombre}', {edad},'{profesion}','{activo}')"
        cursor.execute(query)
        conn.commit()
        conn.close()
        return f'El trabajador {dni} : {nombre} fue dado de alta con exito!'

    except sql.OperationalError as error:
        return error


def buscar(dni):
    try:
        conn = dbOpen()
        cursor = conn.cursor()
        query = "SELECT * FROM trabajadores WHERE dni LIKE ?"
        cursor.execute(query, ["{}".format(dni)])
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
        return datos

    except sql.OperationalError as error:
        return error


def actualizar(id, dni, nombre, edad, profesion, activo):
    try:
        conn = dbOpen()
        cursor = conn.cursor()
        query = "UPDATE trabajadores SET dni = ?, nombre = ?, edad = ?, profesion = ?, activo = ? WHERE id = ?"
        cursor.execute(query, [dni, nombre, edad, profesion, activo, id])
        conn.commit()
        conn.close()
        return f'El trabajador {dni} : {nombre} fue dactualizado con exito!'

    except sql.OperationalError as error:
        return error


def eliminar(dni):
    try:
        conn = dbOpen()
        cursor = conn.cursor()
        query = "DELETE FROM trabajadores WHERE dni = ?"
        cursor.execute(query, ["{}".format(dni)])
        conn.commit()
        conn.close()
        return f"El trabajador {dni} fue eliminado"

    except sql.OperationalError as error:
        return error


def cambiarStatus(dni):
    try:
        conn = dbOpen()
        cursor = conn.cursor()
        query = "DELETE FROM trabajadores WHERE dni = ?"
        cursor.execute(query, ["{}".format(dni)])
        conn.commit()
        conn.close()
        return f"El Status del trabajador {dni} fue cambiado"

    except sql.OperationalError as error:
        return error

def buscarTodos():
    try:
        conn = dbOpen()
        cursor = conn.cursor()
        query = "SELECT * FROM trabajadores"
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
        return datos

    except sql.OperationalError as error:
        return error

def buscarActivos():
    try:
        conn = dbOpen()
        cursor = conn.cursor()
        query = "SELECT * FROM trabajadores WHERE activo='True'"
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
        return datos

    except sql.OperationalError as error:
        return error


def buscarDesocupados():
    try:
        conn = dbOpen()
        cursor = conn.cursor()
        query = "SELECT * FROM trabajadores WHERE activo='False'"
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
        return datos

    except sql.OperationalError as error:
        return error


def buscarProfesion(profesion):
    try:
        conn = dbOpen()
        cursor = conn.cursor()
        query = f"SELECT * FROM trabajadores WHERE profesion LIKE '%{profesion}%'"
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
        return datos

    except sql.OperationalError as error:
        return error


def buscarRango(edad1,edad2):
    try:
        conn = dbOpen()
        cursor = conn.cursor()
        query = f"SELECT * FROM trabajadores WHERE edad >= {edad1} AND edad <= {edad2}"
        cursor.execute(query)
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
        return datos

    except sql.OperationalError as error:
        return error
