import sqlite3
from datetime import datetime


DATABASE = "boby_memory.db"


def conectar():
    return sqlite3.connect(DATABASE)


def crear_tablas():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recuerdos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        tipo TEXT,
        contenido TEXT
    )
    """)

    conexion.commit()
    conexion.close()


def guardar_recuerdo(tipo, contenido):

    crear_tablas()

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO recuerdos
    (fecha, tipo, contenido)
    VALUES (?, ?, ?)
    """,
    (
        datetime.now().strftime("%Y-%m-%d %H:%M"),
        tipo,
        contenido
    ))

    conexion.commit()
    conexion.close()


def obtener_recuerdos(limite=5):

    crear_tablas()

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT fecha, tipo, contenido
    FROM recuerdos
    ORDER BY id DESC
    LIMIT ?
    """,
    (limite,))

    recuerdos = cursor.fetchall()

    conexion.close()

    return recuerdos


# Inicialización automática de Boby
crear_tablas()