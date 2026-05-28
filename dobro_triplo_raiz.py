# ============================================
# 🔴 ENUNCIADO
# Crie um programa que leia um número inteiro
# digitado pelo usuário e calcule:
# - O dobro desse número
# - O triplo desse número
# - A raiz quadrada desse número
# Em seguida, exiba os resultados formatados.
# ============================================

import math

n = int(input("Digite um número: "))

dobro = n * 2
triplo = n * 3
raiz = math.sqrt(n)

print(f"O número é {n}")
print(f"O dobro é {dobro}")
print(f"O triplo é {triplo}")
print(f"A raiz quadrada é {raiz:.2f}")
