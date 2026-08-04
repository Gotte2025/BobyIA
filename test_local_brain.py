from local_brain import generar_respuesta


while True:

    mensaje = input("\nDecile algo a Boby: ")

    respuesta = generar_respuesta(mensaje)

    print("\n🐶 Boby:")
    print(respuesta)