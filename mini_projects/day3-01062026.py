# Day 003 — CLI de conversión de divisas
# Difficulty: Easy | Type: Project
# Time: 25 min | Tags: #cli-tool #api
# Source: propio
# ─────────────────────────────────

import sys
import requests

def convert(amount: float, from_currency: str, to_currency: str) -> float:


    api = requests.get(f"https://open.er-api.com/v6/latest/{from_currency}")
    data = api.json()

    try:
        rate = data["rates"][to_currency]
    except KeyError:
        print(f"Error: la divisa {to_currency} no existe")
        return
    
    conversion = amount * rate

    print(f"{amount} {from_currency} = {conversion:.2f} {to_currency}")

    return conversion

if __name__ == "__main__":
    amount = float(sys.argv[1])
    from_currency = sys.argv[2]
    to_currency = sys.argv[3]

    convert(amount, from_currency, to_currency)

# Aprendizaje: requests.get() llama a una API y .json() convierte la respuesta
# en un diccionario. sys.argv lee los argumentos de la terminal. try/except
# captura errores concretos (KeyError) sin que el programa explote.