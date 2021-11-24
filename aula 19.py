string = "O Brasil é o pais do futebol, o Brasil é penta."


lista = string.split(" ") # separa as palavras da string em lista
print(lista)

"""for valor in lista:
    print("palavra: {} apareceu {} vez(es) " .format(valor, lista.count(valor)))"""

palavra = ""
contagem = 0

for valor in lista:
    qtde_vezes = lista.count(valor)

    if qtde_vezes > contagem:
        contagem = qtde_vezes
        palavra = valor

print("A palavra que apareceu mais vezes é: {}, {} vezes" .format(palavra, contagem))

for i in lista:
    i = i.upper() # converte tudo pra maiusculo
    i = i.strip() # retira todos os espaços
    print(i)

string_2 = "O rato roeu a roupa do rei de Roma"
lista_2 = string_2.split()
string_join = ', '.join(lista_2) #separa cada palavra da string com virgula
print(string_join)
