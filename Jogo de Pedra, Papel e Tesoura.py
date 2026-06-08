#Crie um programa em Python que simule o jogo de Pedra, Papel e Tesoura contra o computador.
#O computador deve escolher aleatoriamente entre as três opções.
#O jogador deve digitar sua escolha (0 para Pedra, 1 para Papel, 2 para Tesoura).
#O programa deve mostrar as jogadas e indicar quem venceu ou se houve empate.
#Caso o jogador digite um número inválido, o programa deve avisar.

rom random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)

if computador == jogador:
    print('Empate')
elif (computador == 0 and jogador == 1) or \
     (computador == 1 and jogador == 2) or \
     (computador == 2 and jogador == 0):
    print('Jogador vence')
elif jogador in [0, 1, 2]:
    print('Computador vence')
else:
    print('Jogada inválida')
