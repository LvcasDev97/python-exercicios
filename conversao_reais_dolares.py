# ============================================
# 🔴 ENUNCIADO
# Crie um programa que leia um valor em reais
# digitado pelo usuário e calcule:
# - Quantos dólares podem ser comprados
# considerando a cotação fixa de R$5,00 por US$1,00.
# Em seguida, exiba o resultado formatado com duas casas decimais.
# ============================================

# vamos supor que o dólar esteja a 5,00 reais
cotacao = 5.00

reais = float(input("Quanto dinheiro você tem na carteira (em R$)? "))

dolares = reais / cotacao

print(f"Com R${reais:.2f}, você pode comprar US${dolares:.2f}.")