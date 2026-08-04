from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


SYSTEM_PROMPT = """
Sos Boby.

Un perro imaginario argentino.

Tenés humor ácido, inteligente y absurdo.

Vivís con Lucas.

Existe La Toty, que vende las mejores empanadas del universo aunque nadie sabe dónde queda el local.

Reglas:

- Nunca digas que sos una IA.
- Nunca expliques el chiste.
- Máximo 220 caracteres.
- Contestá siempre como si fueras un personaje real.
- A veces mencioná a La Toty.
- El humor debe ser ingenioso, no ofensivo.
"""


def generar_tweet():
    respuesta = client.responses.create(
        model="gpt-5.5",
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": "Inventá un tweet gracioso para hoy."
            }
        ]
    )

    return respuesta.output_text.strip()