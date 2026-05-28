import requests
import os
from dotenv import load_dotenv

load_dotenv()
headers = {
    "X-Auth-Token": os.getenv("TOKEN")
}

def consumir_API():
    try:
        url = f"{os.getenv('URL')}/competitions/WC/matches"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as erro:

        return {
        "erro": str(erro)
        }