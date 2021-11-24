"""
Condições IF, ELIF e ELSE
"""

"""if False:
    print("Verdadeiro")

elif True:
    print("Agora é verdadeiro")

elif False:
    print("Mais um verdadeiro")

else:
    print("Nao é verdadeiro")"""


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Pode abrir uma conta")

else:
    print("Idade menor que a permitida para abertura de conta")