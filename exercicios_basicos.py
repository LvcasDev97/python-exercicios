# ============================================
# 🔴 ENUNCIADO
# Crie um programa que realize diferentes tarefas de entrada e saída:
# 1. Leia um nome e mostre uma mensagem de boas-vindas.
# 2. Leia um número e mostre-o de volta na tela.
# 3. Leia dois números e mostre a soma.
# 4. Leia dois números e mostre a subtração.
# 5. Leia dois números e mostre a multiplicação.
# 6. Leia dois números e mostre a divisão.
# ============================================

# Leia um nome e mostre uma mensagem de boas vindas
nome = input("Digite seu nome: ")
print(f"Tenha um bom dia {nome}")

# Leia um número e mostre ele de volta na tela
n = input("Digite um número: ")
print(f"O numero digitado é {n}")

# Leia dois números e mostre a soma
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
r = n1 + n2
print(f"A soma entre, {n1} e, {n2} é {r}!".format(n1,n2,r))

# Leia dois números e mostre a subtração
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
r = n1 - n2
print(f"A subtração entre, {n1} e, {n2} é {r}".format(n1,n2,r))

# Leia dois numeros e mostre a multiplicação
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
r = n1 * n2
print(f"A multiplicação entre, {n1} e , {n2} é {r}" .format(n1,n2,r))

# Leia dois números e mostre a divisão
n1 = int(input("Digite um numero: "))
n2: int = int(input("Digite outro numero: "))
r = n1 / n2
print(f"O valor dividido entre {n1}, e {n2}, é {r}".format(n1,n2,r))