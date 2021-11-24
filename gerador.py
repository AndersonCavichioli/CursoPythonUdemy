from random import choices

qtd = int(input("Quantos jogos deseja? "))
tamanho = int(input("Quantos numeros deseja ? (6 padrão)"))
valores = range(1, 61)

listas = [choices(valores, k=tamanho) for _ in range(qtd)]

for i in listas:
    print(i)