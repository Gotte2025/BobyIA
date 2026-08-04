import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# ==========================
# X API
# ==========================
X_API_KEY = os.getenv("X_API_KEY")
X_API_SECRET = os.getenv("X_API_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")

# ==========================
# OpenAI
# ==========================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def validate_config():
    """
    Verifica que todas las variables necesarias existan.
    """

    required = {
        "X_API_KEY": X_API_KEY,
        "X_API_SECRET": X_API_SECRET,
        "X_ACCESS_TOKEN": X_ACCESS_TOKEN,
        "X_ACCESS_TOKEN_SECRET": X_ACCESS_TOKEN_SECRET,
        "OPENAI_API_KEY": OPENAI_API_KEY,
    }

    missing = []

    for key, value in required.items():
        if value is None or value.strip() == "":
            missing.append(key)

    if missing:
        raise Exception(
            "\n❌ Faltan variables en el archivo .env:\n\n"
            + "\n".join(missing)
        )

    print("✅ Configuración cargada correctamente.")