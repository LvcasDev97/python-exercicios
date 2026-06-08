#Crie um programa em Python que leia o ano de nascimento de uma pessoa e informe sua situação em relação ao alistamento militar:
#Se a idade for exatamente 18 anos, mostre a mensagem: "Você tem que se alistar IMEDIATAMENTE!".
#Se a idade for menor que 18 anos, informe quantos anos faltam para o alistamento e em qual ano ele ocorrerá.
#Se a idade for maior que 18 anos, informe quantos anos já se passaram desde o prazo e em qual ano o alistamento deveria ter ocorrido.

from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {} anos'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(saldo))