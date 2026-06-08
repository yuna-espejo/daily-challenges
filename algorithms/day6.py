# Day 006 — Máximo en una ventana deslizante
# Difficulty: Hard | Type: Algorithm
# Time: 40 min | Tags: #arrays #queue
# Source: LeetCode 239
# ─────────────────────────────────
# Dado un array nums y un entero k, devuelve el máximo de cada
# ventana de tamaño k mientras se desliza de izquierda a derecha.
# ─────────────────────────────────

def max_sliding_window(nums, k):
    valorMaximo = []
    for i in range(len(nums) - k + 1):
        ventana = nums[i:i+k]
        maximo = max(ventana)
        valorMaximo.append(maximo)
    return valorMaximo

print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
print(max_sliding_window([1], 1))                           # [1]

# Complejidad: O(n*k) tiempo, O(n) espacio
# Aprendizaje: slicing nums[i:i+k] extrae la ventana en cada iteración.
# La solución bruta funciona pero es O(n*k). La óptima usa una deque
# monotónica para hacerlo en O(n) — queda pendiente para revisitar.