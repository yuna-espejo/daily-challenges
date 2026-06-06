# Day 002 — Invertir una cadena
# Difficulty: Easy | Type: Algorithm
# Time: 15 min | Tags: #strings #two-pointers
# Source: LeetCode 344
# ─────────────────────────────────

def reverse_string(s: list[str]) -> None:
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i+=1
        j-=1

s = ['h', 'o', 'l', 'a']
reverse_string(s)
print(s)  # ['a', 'l', 'o', 'h']
# ─────────────────────────────────
# Aprendizaje: el patrón two-pointers usa dos índices desde los extremos
# que avanzan hacia el centro. s[i], s[j] = s[j], s[i] intercambia en una
# línea sin variable temporal. while i < j para cuando se cruzan.