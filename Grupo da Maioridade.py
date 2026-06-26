from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a pessoal nasceu?'))
    idade = atual - nasc
    print('Essa pessoa tem {} anos'.format(idade))
    if idade >= 21:
       totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas meiores de idade'.format(totmaior))
print('É também tivemos {} pessoas menores de idade'.format(totmenor))