#Crie um programa em Python que leia duas notas de um aluno e calcule a média.
#Se a média for menor que 5, mostre a mensagem: "O aluno está REPROVADO".
#Se a média estiver entre 5 e 7, mostre: "O aluno está em RECUPERAÇÃO".
#Se a média for maior ou igual a 7, mostre: "O aluno está APROVADO".
#O programa deve exibir também as notas digitadas e a média calculada.

nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 >média > 5:
    print('O aluno está em RECUPERAÇÂO')
elif média < 5:
    print('O aluno está REPROVADO')
elif média >= 7:
    print('O aluno está APROVADO')
