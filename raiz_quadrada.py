# ============================================
# 🔴 ENUNCIADO
# Crie um programa que leia um número inteiro
# digitado pelo usuário e calcule:
# - A raiz quadrada desse número
# Em seguida, exiba o resultado formatado com duas casas decimais.
# ============================================

import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {:.2f}".format(num, raiz))