# ============================================
# 🔴 ENUNCIADO
# Crie um programa que simule a análise de um financiamento
# para compra de uma casa. O programa deve:
# - Ler o valor da casa
# - Ler o salário do comprador
# - Ler em quantos anos será feito o financiamento
# - Calcular o valor da prestação mensal
# - Verificar se a prestação não ultrapassa 30% do salário
# - Informar se o empréstimo pode ser concedido ou não
# ============================================

casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento?'))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')