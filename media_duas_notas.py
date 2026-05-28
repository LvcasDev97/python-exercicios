# ============================================
# 🔴 ENUNCIADO
# Crie um programa que leia duas notas de um aluno
# (valores decimais) e calcule:
# - A média aritmética entre elas
# Em seguida, exiba o resultado formatado com duas casas decimais.
# ============================================

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

media = (n1 + n2) / 2

print(f"A média do aluno é {media:.2f}")