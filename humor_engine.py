import random


RESPUESTAS = {

    "aburrido": [
        "Boby dice que el aburrimiento es la señal de que falta una empanada de la Toty.",
        "La Toty tiene una empanada contra el aburrimiento. No funciona, pero está rica."
    ],

    "lunes": [
        "Boby sospecha que el lunes fue inventado por alguien que odiaba los perros felices.",
        "La Toty intentó vender empanadas anti-lunes. Se agotaron antes de existir."
    ],

    "trabajo": [
        "Boby fue a trabajar una vez. Lo echaron por dormir en modo profesional.",
        "La Toty dice que trabajar da hambre. Por eso inventó la empanada de supervivencia."
    ],

    "comida": [
        "Boby abrió la heladera y encontró una nota de la Toty: 'No tocar mis empanadas'."
    ]
}


def analizar_humor(mensaje):

    texto = mensaje.lower()

    for palabra, respuestas in RESPUESTAS.items():

        if palabra in texto:
            return random.choice(respuestas)

    return None