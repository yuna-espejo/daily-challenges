# Day 001 — Two Sum
# Difficulty: Easy | Type: Algorithm
# Time: 35 min | Tags: #arrays #hashmap
# Source: LeetCode 1
# ─────────────────────────────────
# Dado un array y un target, devuelve índices de los dos números que sumen target.
# ─────────────────────────────────

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {} # diccionario vacío

    for i, num in enumerate(nums): # i = indice, num = valor
        complement = target - num # lo que necesito encontrar

        if complement in seen: # revisar si lo vi antes
            return [seen[complement], i] # si? devuelvo los dos indices
        
        seen[num] = i # no? guardo el número y su índice para seguir

        

print(two_sum([3, 2, 4], 6))

# ─────────────────────────────────
# Aprendizaje: el doble bucle funciona pero es O(n²). Con un diccionario
# guardas los números vistos y encuentras el complemento en O(1), una sola pasada.