# ============================================
# 🔴 ENUNCIADO
# Crie um programa que utilize a biblioteca `emoji`
# para exibir uma mensagem contendo texto e um emoji.
# - A mensagem deve incluir "Olá mundo"
# - O emoji exibido deve ser o da Terra 🌎
# ============================================

import emoji
print(emoji.Emoji("Olá mundo :earth_americas:", use_aliases=True))