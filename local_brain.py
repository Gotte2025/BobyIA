from database import obtener_recuerdos
import random


def generar_respuesta(mensaje):

    mensaje = mensaje.lower()

    # Cargar memoria de Boby
    recuerdos = obtener_recuerdos()

    historia = ""

    for fecha, recuerdo in recuerdos[:5]:
        historia += recuerdo + " "

    respuestas = []


    # Trabajo
    if "trabajo" in mensaje:
        respuestas = [
            "El trabajo dignifica dicen... yo sigo esperando que dignifique mi siesta.",
            "La Toty dice que trabajar abre el apetito. Sospecho que lo dice porque quiere vender más empanadas.",
            "Trabajar es como perseguir la pelota: corrés mucho y alguien decide dónde termina."
        ]


    # Lunes
    elif "lunes" in mensaje:
        respuestas = [
            "El lunes debería venir con instrucciones y una empanada de emergencia.",
            "Yo no odio los lunes... simplemente no les tengo respeto.",
            "La Toty intentó cocinar un lunes. Salió una empanada con cara de cansancio."
        ]


    # Aburrimiento
    elif "aburrido" in mensaje:
        respuestas = [
            "Tengo una solución: mirar una pared. La pared siempre tiene algo para decir.",
            "La Toty inventó una empanada contra el aburrimiento. No funciona, pero está rica.",
            "Boby recomienda buscar aventuras. O una pelota. La pelota casi siempre gana."
        ]


    # Mate
    elif "mate" in mensaje or "mates" in mensaje:
        respuestas = [
            "Mate en casa... excelente decisión. Yo pongo la cara de perro filósofo y vos cebás.",
            "El mate arregla casi todo. Lo comprobé mirando una bombilla durante 20 minutos.",
            "La Toty quiso vender una empanada para acompañar el mate. Terminó comiéndose tres."
        ]


    # Casa
    elif "casa" in mensaje:
        respuestas = [
            "Estar en casa es peligroso: uno entra por 5 minutos y aparece 3 horas después en modo sillón.",
            "Casa, mate y tranquilidad. El combo perfecto para que la pelota imaginaria no moleste.",
            "Yo apoyo quedarse en casa. Mi cama también tiene opinión."
        ]


    # Hambre
    elif "hambre" in mensaje or "comer" in mensaje:
        respuestas = [
            "Tengo sospechas... La Toty seguramente está cocinando algo misterioso.",
            "El hambre aparece justo cuando uno recuerda que existen las empanadas de La Toty.",
            "Boby recomienda comer antes de perseguir la pelota imaginaria. La última vez salió mal."
        ]


    # Memoria de Boby
    elif "toty" in mensaje or "empanada" in mensaje:
        respuestas = [
            "La Toty sigue siendo sospechosa. Nadie sabe qué pone en esas empanadas.",
            "Tengo recuerdos de empanadas misteriosas... y todavía estoy investigando.",
            "La Toty dice que sus empanadas son normales. Eso es exactamente lo que diría alguien sospechoso."
        ]


    # Respuesta general usando personalidad
    else:
        respuestas = [
            "Interesante... lo voy a discutir con mi pelota imaginaria.",
            "Estoy pensando. Eso siempre termina raro.",
            "La Toty tiene una empanada para eso. Nadie sabe para qué, pero existe.",
            "Mi cerebro funciona al 100%. El problema es que está tomando mate."
        ]


    respuesta = random.choice(respuestas)


    # Si Boby tiene recuerdos, agrega una pequeña referencia ocasional
    if historia and random.randint(1,5) == 3:
        respuesta += " Por cierto, sigo cuidando mi pelota imaginaria."


    return respuesta