"""
diminuir linhas de codigo com expressao condicional
"""

nome = input("Digite seu nome: ")
print(nome or "Voce nao digitou nada")

#Esse código abaixo faz exatamente a mesma coisa que o codigo acima
if nome:
    print(nome)
else:
    print("Voce não digitou nada")