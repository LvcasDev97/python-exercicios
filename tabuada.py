# ============================================
# 🔴 ENUNCIADO
# Crie um programa que leia um número inteiro
# digitado pelo usuário e exiba a tabuada desse número,
# mostrando os resultados da multiplicação de 1 até 10.
# ============================================

n = int(input("Digite um número: "))

print(f"Tabuada do {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")