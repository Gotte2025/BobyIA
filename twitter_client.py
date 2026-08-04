import tweepy

from config import (
    X_API_KEY,
    X_API_SECRET,
    X_ACCESS_TOKEN,
    X_ACCESS_TOKEN_SECRET
)


def crear_cliente():

    client = tweepy.Client(
        consumer_key=X_API_KEY,
        consumer_secret=X_API_SECRET,
        access_token=X_ACCESS_TOKEN,
        access_token_secret=X_ACCESS_TOKEN_SECRET
    )

    return client



def verificar_conexion():

    client = crear_cliente()

    usuario = client.get_me()

    if usuario.data:
        print("🐦 Conectado a X")
        print(
            f"Usuario: @{usuario.data.username}"
        )
    else:
        print("❌ No se pudo conectar")