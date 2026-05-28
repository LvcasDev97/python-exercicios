# ============================================
# 🔴 ENUNCIADO
# Crie um programa que leia um valor em metros
# digitado pelo usuário e calcule:
# - O equivalente em centímetros
# - O equivalente em milímetros
# Em seguida, exiba os resultados formatados.
# ============================================

metros = float(input("Digite um valor em metros: "))

centimetros = metros * 100
milimetros = metros * 1000

print(f"{metros} metros equivalem a {centimetros:.0f} centímetros e {milimetros:.0f} milímetros.")