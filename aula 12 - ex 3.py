"""
faça um programa que peça o primeiro nome ao usuario, se o nome tiver 4 letras ou menos escreva "Seu nome é curto", se tiver
5 e 6 letras "Seu nome e normal" e se for maior q 6 "seu nome e muito grande"
"""

nome = input("Digite seu nome: ")
tamanho = len(nome)

if nome.isalpha():

    if tamanho <= 4:
        print("Seu nome é muito curto!")
    elif tamanho >= 5 and tamanho <= 6:
        print("Seu nome é normal!")

    else:
        print("Seu nome é muito grande!")
else:
    print(f"{nome} não é válido como um nome")