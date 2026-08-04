from local_brain import generar_respuesta
from memory_manager import analizar_y_guardar


print("🐶 Boby IA listo")
print("Escribí salir para terminar\n")


while True:

    mensaje = input("Vos: ")

    if mensaje.lower() == "salir":
        print("\n🐶 Boby:")
        print("Me voy a dormir arriba de mi pelota imaginaria.")
        break


    respuesta = generar_respuesta(mensaje)

    analizar_y_guardar(mensaje)


    print("\n🐶 Boby:")
    print(respuesta)
    print()