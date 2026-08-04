from database import (
    crear_tablas,
    guardar_recuerdo,
    obtener_recuerdos
)


crear_tablas()

guardar_recuerdo(
    "historia",
    "Boby encontró una pelota y dice que ahora es su tesoro."
)


guardar_recuerdo(
    "toty",
    "La Toty inventó una empanada sabor misterio."
)


print("🧠 Recuerdos de Boby:")

for recuerdo in obtener_recuerdos():
    print(recuerdo)