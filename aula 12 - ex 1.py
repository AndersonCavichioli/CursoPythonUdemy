"""
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou impar. Caso o usuario nao figite um numero
inteiro, informe que nao é um numero inteiro.
"""

n = input("Digite um numero: ")

if n.isdigit():
    n = int(n)

    if n % 2 == 0:
        print(f"Numero {n} par")

    else:
        print(f"Numero {n} impar")

else:
    print("Esse numero nao e inteiro")

