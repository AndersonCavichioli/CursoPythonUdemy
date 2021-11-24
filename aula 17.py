"""
listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

#         0    1    2    3
lista = ["a", "b", "c", "d"]
print(lista[1]) #mostra na tela a posição 1 da lista acima

print(lista[::-1]) #mostra na tela a lista invertida

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2 #o operador de + aqui concatena as listas, juntando as 2
l4 = [1, 5, 8, 15, 45, 78, 6]

print(l1) #mostra a lista l1
print(l2) #mostra a lista l2
print(l3) #mostra a lista l1 junto com a lista l2

l1.extend(l2) #faz o mesmo que a variavel acima, porem modifica a l1 pra extender com a l2
l1.extend('anderson') #extende a lista com os caracteres do nome "anderson" criando uma posicao pra cada letra
print(l1)

l2.append('b') #acrescenta o valor ao final da lista
print(l2)

l2.insert(0, 'abacaxi') #insere na posição 0 a string abacaxi, sem alterar as demais
print(l2)

l2.pop() # deleta o ultimo valor da lista
print(l2)

del(l2[0]) #deleta da variavel L2 a posição 0
print(l2)

print(max(l4)) #mostra o valor maior da lista

l5 = list(range(0, 101, 5)) #cria a variavel 5, transforma em lista e coloca os valores de 0 a 100 nela, alterando por multiplos de 5
print(l5)

for valor in l5: #mostra todos os valores contidos na lista
    print(valor)

soma = 0
for valor in l5:
    soma = soma + valor
    print(f'{soma} + {valor} = {soma}')
print(soma)
