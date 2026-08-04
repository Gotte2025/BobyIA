from prompts import boby_system_prompt
from database import obtener_recuerdos


def crear_contexto_memoria():

    recuerdos = obtener_recuerdos(5)

    if not recuerdos:
        return "Boby todavía no tiene recuerdos."

    texto = "Recuerdos anteriores de Boby:\n"

    for fecha, contenido in recuerdos:
        texto += f"- {fecha}: {contenido}\n"

    return texto



def preparar_mente_boby():

    personalidad = boby_system_prompt()

    memoria = crear_contexto_memoria()

    cerebro = f"""
{personalidad}

==============================

MEMORIA:

{memoria}

==============================

Usá estos recuerdos para mantener continuidad.
No inventes que olvidaste historias anteriores.
"""

    return cerebro