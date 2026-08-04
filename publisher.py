from twitter_client import crear_cliente


def publicar_tweet(texto):

    client = crear_cliente()

    respuesta = client.create_tweet(
        text=texto
    )

    return respuesta