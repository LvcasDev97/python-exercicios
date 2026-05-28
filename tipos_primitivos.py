# ============================================
# 🔴 ENUNCIADO
# Crie um programa que leia diferentes tipos de dados
# fornecidos pelo usuário e demonstre o uso de tipos primitivos:
# - Um número inteiro (idade)
# - Uma string (nome)
# - Um valor booleano (gosta de programação: sim/não)
# Em seguida, exiba uma mensagem personalizada com os dados coletados.
# ============================================

# 1. Inteiro
idade = int(input("Digite sua idade: "))

# 2. String
nome = input("Digite seu nome: ")

# 3. Booleano
resposta = input("Você gosta de programação? (sim/não): ")
gosta_programar = resposta.lower() == "sim"  # True se sim, False se não

# 4. Print
print("Olá,", nome, "! Você tem", idade, "anos.")
print("Gosta de programação?", gosta_programar)

