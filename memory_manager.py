from database import guardar_recuerdo, obtener_recuerdos


def analizar_y_guardar(mensaje):

    mensaje_original = mensaje
    mensaje = mensaje.lower()

    recuerdo = None


    # Memoria del usuario

    if "mate" in mensaje or "mates" in mensaje:
        recuerdo = "Lucas estaba tomando mates."


    elif "trabajo" in mensaje or "trabajar" in mensaje:
        recuerdo = "Lucas habló sobre el trabajo."


    elif "casa" in mensaje or "hogar" in mensaje:
        recuerdo = "Lucas estaba en casa."


    elif "hambre" in mensaje or "comer" in mensaje:
        recuerdo = "Lucas tenía hambre y pensó en comida."


    elif "cansado" in mensaje or "cansada" in mensaje:
        recuerdo = "Lucas comentó que estaba cansado."


    # Memoria del universo de Boby

    elif "toty" in mensaje or "empanada" in mensaje:
        recuerdo = "Lucas mencionó a La Toty y sus empanadas misteriosas."


    elif "pelota" in mensaje:
        recuerdo = "Boby recordó su pelota imaginaria."


    if recuerdo:

        # Evitar duplicados
        recuerdos = obtener_recuerdos()

        for fecha, texto in recuerdos:
            if texto == recuerdo:
                return False


        guardar_recuerdo(
            "usuario",
            recuerdo
        )

        return True


    return False
