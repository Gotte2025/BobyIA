from database import obtener_recuerdos
import random
import unicodedata


def quitar_acentos(texto):

    return "".join(
        c
        for c in unicodedata.normalize("NFD", texto)
        if unicodedata.category(c) != "Mn"
    )


def generar_respuesta(mensaje):

    mensaje_original = mensaje

    mensaje = mensaje.lower()
    mensaje = quitar_acentos(mensaje)


    # =========================
    # CARGAR MEMORIA DE BOBY
    # =========================

    recuerdos = obtener_recuerdos(20)

    historia = []
    nombre_usuario = None


    for fecha, tipo, recuerdo in recuerdos:

        historia.append(recuerdo)

        if tipo == "usuario_nombre":

            nombre_usuario = (
                recuerdo
                .replace("El usuario se llama ", "")
                .strip()
            )


    respuestas = []


    # =========================
    # QUE SABE BOBY DEL USUARIO
    # =========================

    if (
        "que sabes de mi" in mensaje
        or "que sabes sobre mi" in mensaje
        or "que recordas de mi" in mensaje
        or "recordas de mi" in mensaje
        or "sabes de mi" in mensaje
    ):

        datos = []


        for fecha, tipo, recuerdo in recuerdos:

            if tipo == "usuario_nombre":

                datos.append(
                    recuerdo.replace(
                        "El usuario se llama ",
                        ""
                    )
                )


            elif tipo == "usuario":

                datos.append(recuerdo)


        if datos:

            respuesta = "Según mi memoria, "


            if nombre_usuario:

                respuesta += f"sos {nombre_usuario}. "


            if any("mate" in dato.lower() for dato in datos):

                respuesta += (
                    "Sé que te gusta compartir mates conmigo. "
                )


            if any(
                "hambre" in dato.lower()
                or "comida" in dato.lower()
                for dato in datos
            ):

                respuesta += (
                    "También recuerdo que hablamos de comida. "
                )


            if any(
                "trabajo" in dato.lower()
                for dato in datos
            ):

                respuesta += (
                    "Recuerdo que mencionaste temas de trabajo. "
                )


            respuesta += (
                "La Toty sigue bajo investigación por sus empanadas misteriosas."
            )


            return respuesta


        else:

            return (
                "Todavía no tengo suficientes recuerdos sobre vos."
            )


    # =========================
    # COMO ME LLAMO
    # =========================

    elif (
        "como me llamo" in mensaje
        or "cual es mi nombre" in mensaje
        or "quien soy" in mensaje
    ):


        if nombre_usuario:

            respuestas = [
                f"Te llamás {nombre_usuario}. Lo tengo guardado en mi memoria.",
                f"Sos {nombre_usuario}. Ya sos parte de la historia de Boby.",
                f"Claro que sé quién sos {nombre_usuario}. No me hagas perder la pelota imaginaria."
            ]


        else:

            respuestas = [
                "Todavía no sé tu nombre. Presentate y lo guardo.",
                "Mi memoria necesita ese dato."
            ]



    # =========================
    # TE ACORDAS DE MI
    # =========================

    elif (
        "te acordas de mi" in mensaje
        or "te acordas" in mensaje
        or "te acordas quien soy" in mensaje
    ):


        if nombre_usuario:

            respuestas = [
                f"Obvio {nombre_usuario}. Ya estás guardado en mi memoria.",
                f"Claro {nombre_usuario}. Sos el humano de los mates y las preguntas interesantes.",
                f"Me acuerdo de vos {nombre_usuario}. Mi memoria funciona mejor que mi puntería con la pelota."
            ]

        else:

            respuestas = [
                "Todavía no sé quién sos. Tenemos que presentarnos.",
                "Mi memoria está empezando a conocerte."
            ]



    # =========================
    # NOMBRE NUEVO
    # =========================

    elif (
        "soy " in mensaje
        or "me llamo " in mensaje
    ):


        respuestas = [
            "Perfecto. Voy a guardar ese dato en mi memoria.",
            "Registrado. Mi cerebro de perro imaginario aprendió algo nuevo.",
            "Excelente. Ahora tengo un humano identificado."
        ]



    # =========================
    # TRABAJO
    # =========================

    elif "trabajo" in mensaje:

        respuestas = [

            "El trabajo dignifica dicen... yo sigo esperando que dignifique mi siesta.",

            "La Toty dice que trabajar abre el apetito. Sospecho que quiere vender más empanadas.",

            "Trabajar es como perseguir la pelota: corrés mucho y alguien decide dónde termina."

        ]



    # =========================
    # MATE
    # =========================

    elif "mate" in mensaje or "mates" in mensaje:

        respuestas = [

            "Mate en casa... excelente decisión. Yo pongo cara de perro filósofo y vos cebás.",

            "El mate arregla casi todo. Lo comprobé mirando una bombilla durante 20 minutos.",

            "La Toty quiso vender una empanada para acompañar el mate. Terminó comiéndose tres."

        ]



    # =========================
    # CASA
    # =========================

    elif "casa" in mensaje or "hogar" in mensaje:

        respuestas = [

            "Estar en casa es peligroso: uno entra 5 minutos y aparece 3 horas después en modo sillón.",

            "Casa, mate y tranquilidad. El combo perfecto.",

            "Yo apoyo quedarse en casa. Mi cama también tiene opinión."

        ]



    # =========================
    # HAMBRE
    # =========================

    elif "hambre" in mensaje or "comer" in mensaje:

        respuestas = [

            "Tengo sospechas... La Toty seguramente está cocinando algo misterioso.",

            "El hambre aparece cuando uno recuerda que existen las empanadas de La Toty.",

            "Boby recomienda comer antes de perseguir la pelota imaginaria."

        ]



    # =========================
    # TOTY
    # =========================

    elif "toty" in mensaje or "empanada" in mensaje:

        respuestas = [

            "La Toty sigue siendo sospechosa. Nadie sabe qué pone en esas empanadas.",

            "Tengo recuerdos de empanadas misteriosas... sigo investigando.",

            "La Toty dice que sus empanadas son normales. Eso es exactamente lo que diría alguien sospechoso."

        ]



    # =========================
    # GENERAL
    # =========================

    else:

        respuestas = [

            "Interesante... lo voy a discutir con mi pelota imaginaria.",

            "Estoy pensando. Eso siempre termina raro.",

            "La Toty tiene una empanada para eso. Nadie sabe para qué, pero existe.",

            "Mi cerebro funciona al 100%. El problema es que está tomando mate."

        ]


    respuesta = random.choice(respuestas)


    # referencia ocasional

    if historia and random.randint(1,5) == 3:

        respuesta += (
            " Por cierto, sigo cuidando mi pelota imaginaria."
        )


    return respuesta