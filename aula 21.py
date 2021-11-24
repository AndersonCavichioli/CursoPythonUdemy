"""
desempacotamento python
"""

lista = ["Luiz", "Joao", "Maria"]

n1, n2, n3 = lista #vincula n1 a primeira posição na lista

print(n1)

lista_2 = ["Carlos", "Rodrigo", "Ana", 1, 2, 3, 4, 5, 6, 7]

x1, x2, x3, *nova_variavel = lista_2 #o * vincula uma nova variavel para as demais posições na lista

print(nova_variavel)

lista_3 = ["Beatriz", "Anderson", "Antonio", 1, 2, 3, 4, 5, 6, 7, 100]

x1, x2, *nova_variavel, ultima_posicao = lista_3 #atribui o ultimo elemento da lista na variavel ultima_posicao

print(ultima_posicao)

