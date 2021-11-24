"""string = "Testando um texto que esta dentro de uma variável"
lista = string.split()


for a, b in enumerate(lista): #a recebe a variavel enumerate e b recebe cada iteravel da lista

    print(a, b)"""

#Esse código abaixo é a mesma coisa que o codigo acima, porem, sem usar a funcao enumerate

lista_2 = [

[0, 'manha'],
[1, 'tarde'],
[2, 'noite']

          ]

for indice, nome in lista_2:
    print(indice, nome)
