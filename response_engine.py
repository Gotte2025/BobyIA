from humor_engine import analizar_humor
from random import choice


FRASES_BOBY = [
    "Boby sigue investigando por qué las medias desaparecen en el lavarropas.",
    "La Toty dice que todo problema mejora con una empanada."
]


def generar_respuesta(mensaje):

    print("🧠 Analizando mensaje:")
    print(mensaje)

    respuesta = analizar_humor(mensaje)

    if respuesta:
        return respuesta

    return choice(FRASES_BOBY)