# ============================================
# 🔴 ENUNCIADO
# Crie um programa que leia dois números inteiros
# digitados pelo usuário e mostre:
# - A soma entre eles
# - A mensagem formatada exibindo os valores e o resultado
# ============================================

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
#print('A soma entre n1 e n2 é {}'.format(s))
print('A soma entre {} e {} vale {}'.format(n1, n2, s))