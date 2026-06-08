#Crie um programa em Python que leia o valor de uma compra e ofereça opções de pagamento:
#[1] À vista no dinheiro/Pix → 10% de desconto.
#[2] À vista no cartão → 5% de desconto.
#[3] Em 2x no cartão → preço normal, sem juros.
#[4] Em 3x ou mais no cartão → preço com 20% de juros.
#O programa deve calcular o valor final da compra de acordo com a opção escolhida, mostrar o valor das parcelas (quando houver) e exibir o total a ser pago.
#Se o usuário digitar uma opção inválida, o programa deve considerar o preço normal sem desconto.

print('{:=^40}'.format(' LOJAS SILVA '))
preço = float(input('Preço das compras: R$'))
print(''' FORMAS DE PAGAMENTO
[1] à vista no dinheiro/Pix
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    totparc = int(input('Quantas parcelas? '))
    total = preço + (preço * 20 / 100)
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('Opção inválida, será considerado preço normal.')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
