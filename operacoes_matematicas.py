# ============================================
# 🔴 ENUNCIADO
# Crie um programa que leia dois números inteiros
# digitados pelo usuário e calcule:
# - A soma entre eles
# - O produto (multiplicação)
# - A divisão (com casas decimais)
# - A divisão inteira
# - A potência (primeiro número elevado ao segundo)
# Em seguida, exiba os resultados formatados de forma clara.
# ============================================

n1 = int(input('um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e a  \n divisão é {:.3f}'.format(s, m, d), end='')
print('A Divisão inteira {} e potência {}'.format(di, e))
