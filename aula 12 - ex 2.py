"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada.
"""

h = input("Digite a hora: ")

if h.isdigit():
    h = int(h)

    if h >= 0 and h <= 11:
        print("Bom dia")

    elif h >= 12 and h <= 17:
        print("Boa tarde")

    elif h >= 18 and h <= 23:
        print("Boa noite")

else:
    print("Horario invalido")

