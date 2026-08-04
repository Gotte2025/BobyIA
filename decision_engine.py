import random


def evaluar_mensaje(mensaje):

    texto = mensaje.lower()

    resultado = {
        "responder": False,
        "tipo": "normal",
        "prioridad": 0
    }


    palabras_humor = [
        "lunes",
        "trabajo",
        "cansado",
        "aburrido",
        "comida",
        "café",
        "mate"
    ]


    for palabra in palabras_humor:

        if palabra in texto:
            resultado["responder"] = True
            resultado["tipo"] = "humor"
            resultado["prioridad"] = 80
            return resultado


    palabras_emocionales = [
        "triste",
        "murió",
        "perdí",
        "enfermo"
    ]


    for palabra in palabras_emocionales:

        if palabra in texto:
            resultado["responder"] = True
            resultado["tipo"] = "empatía"
            resultado["prioridad"] = 90
            return resultado


    # pequeño porcentaje de respuesta espontánea
    if random.random() > 0.8:
        resultado["responder"] = True
        resultado["tipo"] = "curiosidad"
        resultado["prioridad"] = 40


    return resultado