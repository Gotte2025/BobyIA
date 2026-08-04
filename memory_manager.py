from database import guardar_recuerdo, obtener_recuerdos
import re


def obtener_nombre_usuario():

    recuerdos = obtener_recuerdos(20)

    for fecha, tipo, contenido in recuerdos:

        if tipo == "usuario_nombre":
            return contenido.replace("El usuario se llama ", "")

    return None



def analizar_y_guardar(mensaje):

    mensaje_original = mensaje
    mensaje = mensaje.lower()

    recuerdo = None
    tipo = "usuario"


    # =========================
    # DETECTAR NOMBRE
    # =========================

    patrones = [
        r"soy ([a-záéíóúñ]+)",
        r"me llamo ([a-záéíóúñ]+)",
        r"mi nombre es ([a-záéíóúñ]+)"
    ]


    for patron in patrones:

        resultado = re.search(patron, mensaje)

        if resultado:

            nombre = resultado.group(1).capitalize()

            recuerdo = f"El usuario se llama {nombre}"
            tipo = "usuario_nombre"

            break



    # =========================
    # MEMORIA USUARIO
    # =========================

    if recuerdo is None:


        if "mate" in mensaje or "mates" in mensaje:
            recuerdo = "El usuario estaba tomando mates."


        elif "trabajo" in mensaje or "trabajar" in mensaje:
            recuerdo = "El usuario habló sobre el trabajo."


        elif "casa" in mensaje or "hogar" in mensaje:
            recuerdo = "El usuario estaba en casa."


        elif "hambre" in mensaje or "comer" in mensaje:
            recuerdo = "El usuario tenía hambre y pensó en comida."


        elif "cansado" in mensaje or "cansada" in mensaje:
            recuerdo = "El usuario comentó que estaba cansado."


    # =========================
    # UNIVERSO BOBY
    # =========================

    if recuerdo is None:


        if "toty" in mensaje or "empanada" in mensaje:

            recuerdo = "El usuario mencionó a La Toty y sus empanadas misteriosas."
            tipo = "toty"



        elif "pelota" in mensaje:

            recuerdo = "Boby recordó su pelota imaginaria."
            tipo = "historia"



    # =========================
    # GUARDAR
    # =========================

    if recuerdo:


        recuerdos = obtener_recuerdos(50)


        for fecha, tipo_guardado, contenido in recuerdos:

            if contenido == recuerdo:
                return False



        guardar_recuerdo(
            tipo,
            recuerdo
        )

        return True



    return False