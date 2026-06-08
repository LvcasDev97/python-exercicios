#Crie um programa em Python que leia o comprimento de três segmentos de reta e determine se eles podem formar um triângulo.
#Para formar um triângulo, cada segmento deve ser menor que a soma dos outros dois.
#Caso seja possível formar um triângulo, classifique-o em:
#Equilátero → todos os lados iguais.
#Isósceles → dois lados iguais.
#Escaleno → todos os lados diferentes.
#Caso contrário, informe que os segmentos não podem formar um triângulo.

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
     print('Os segmentos acima PODEM FORMAR um triângulo' , end='')
     if r1 == r2 == r3:
         print('EQUILATERO')
     elif r1 != r2 != r3 != r1:
         print('ESCALENO')
     else:
         print('ISÒCELES')
else:
 print('Os segmentos acima NÂO PODEM FORMAR triângulo')
