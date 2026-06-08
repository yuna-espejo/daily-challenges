# Day 004 — Número válido de palíndromo
# Difficulty: Easy | Type: Algorithm
# Time: 20 min | Tags: #strings #two-pointers
# Source: LeetCode 125
# ─────────────────────────────────
# Determina si una frase es palíndromo ignorando espacios,
# signos de puntuación y mayúsculas.
# ─────────────────────────────────

def limpiarFrase(frase):
    minusc = frase.lower()
    fraseLimpia = ""
    for caracter in minusc:
        if caracter.isalnum():
            fraseLimpia += caracter
    return fraseLimpia

def comprobarFrase(fraseLimpia):
    invertida = fraseLimpia[::-1]
    if fraseLimpia == invertida:
        return True
    else:
        return False

print(comprobarFrase(limpiarFrase("A man, a plan, a canal: Panama")))  # True
print(comprobarFrase(limpiarFrase("race a car")))                       # False
print(comprobarFrase(limpiarFrase(" ")))                                # True

# Complejidad: O(n) tiempo, O(n) espacio
# Aprendizaje: limpiar primero con isalnum() y lower(), luego comparar
# el string con su inverso [::-1]. Separar en dos funciones hace el código
# más legible y reutilizable.