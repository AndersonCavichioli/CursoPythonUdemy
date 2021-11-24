"""
Função len (contar caracteres)
"""

"""nome = input("Qual o seu nome: ")

print(nome, len(nome), type(nome))

if len(nome) < 8:
    print("O nome nao esta completo")

else:
    print("O nome esta completo")"""

a = input("Digite nome: ")
b = input("Digite sobrenome: ")

print("O nome tem: {} letras e o sobre nome tem: {} letras. O total de caracteres é de: {} letras" .format(len(a), len(b), len(a) + len(b)))

