#Crie um programa em Python que leia dois números inteiros e compare-os.
#Se o primeiro número for maior, mostre a mensagem: "O PRIMEIRO valor é maior".
#Se o segundo número for maior, mostre: "O SEGUNDO valor é maior".
#Caso os dois números sejam iguais, mostre: "Os dois valores são IGUAIS".

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n1 < n2:
    print('O SEGUNDO valor é maior ')
else:
    print('Os dois vslores são IGUAIS')