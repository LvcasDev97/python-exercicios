#Crie um programa em Python que leia o peso e a altura de uma pessoa, calcule o seu Índice de Massa Corporal (IMC) e mostre a classificação correspondente:
#IMC abaixo de 18.5 → Abaixo do peso
#IMC entre 18.5 e 25 → Peso normal
#IMC entre 25 e 30 → Sobrepeso
#IMC entre 30 e 40 → Obesidade
#IMC acima de 40 → Obesidade mórbida
#O programa deve exibir o valor do IMC calculado com uma casa decimal e a mensagem adequada à faixa encontrada.

peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO do PESO normal')
elif 18.5 <= imc <= 25:
    print('PARABÉNS, você está na faixa de PESO normal')
elif 25 < imc < 30:
    print('Você está com SOBREPESO')
elif 30 < imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
