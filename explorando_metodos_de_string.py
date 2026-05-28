# ============================================
# 🔴 ENUNCIADO
# Crie um programa que leia uma entrada do usuário
# e mostre diferentes informações sobre o conteúdo digitado:
# - O tipo primitivo do valor
# - Se contém apenas espaços
# - Se é numérico
# - Se é alfabético
# - Se é alfanumérico
# - Se está em maiúsculas
# - Se está em minúsculas
# - Se está capitalizado (primeira letra maiúscula)
# ============================================

a = input ('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanúmerico? ', a.isalnum())
print('Está em maiusculas? ', a.isupper())
print('Está em minusculas? ', a.islower())
print('Está capitalizada? ', a.istitle())
