from config import validate_config
from openai_client import generar_tweet


def main():

    print("🐶 Iniciando Boby IA...\n")

    validate_config()

    print("\n🧠 Pensando...")

    tweet = generar_tweet()

    print("\n==============================")
    print(tweet)
    print("==============================\n")


if __name__ == "__main__":
    main()