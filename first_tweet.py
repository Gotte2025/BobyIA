from publisher import publicar_tweet


tweet = """
🐶 Hola, soy Boby.

Perro imaginario argentino.
Experto en opinar de lunes, mates y empanadas.

La Toty cocina...
yo pruebo y critico. 🥟
"""


print("Preparando tweet:")
print(tweet)


respuesta = publicar_tweet(tweet)

print("\n✅ Tweet publicado")
print(respuesta)