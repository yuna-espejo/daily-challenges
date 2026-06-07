# Day 005 — Generador de contraseñas
# Difficulty: Easy | Type: Project
# Time: 28 min | Tags: #cli-tool #automation
# Source: propio
# ─────────────────────────────────
# Genera una contraseña aleatoria según los flags que pase el usuario.
# Por defecto solo letras y longitud 8. Añade --numbers y/o --symbols.
# Uso: python passgen.py --length 16 --symbols --numbers
# ─────────────────────────────────

import string
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('--symbols', action='store_true', help='Incluir símbolos')
parser.add_argument('--numbers', action='store_true', help='Incluir números')
parser.add_argument('--length', type=int, default=8, help='Longitud de la contraseña')
args = parser.parse_args()

pool = string.ascii_lowercase + string.ascii_uppercase
if args.numbers:
    pool += string.digits
if args.symbols:
    pool += string.punctuation

password = ""
for i in range(args.length):
    password += random.choice(pool)

print(password)

# Complejidad: O(n) donde n es la longitud de la contraseña
# Aprendizaje: argparse gestiona flags de CLI de forma limpia (--flag activa
# store_true, type=int convierte el valor). El pool se construye sumando
# strings de caracteres y random.choice elige uno al azar en cada iteración.