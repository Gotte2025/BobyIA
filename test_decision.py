from decision_engine import evaluar_mensaje


mensajes = [
    "Estoy cansado del trabajo",
    "Hoy estoy triste",
    "Que lindo día",
    "Odio los lunes"
]


for m in mensajes:

    print("\nMensaje:")
    print(m)

    print(
        evaluar_mensaje(m)
    )