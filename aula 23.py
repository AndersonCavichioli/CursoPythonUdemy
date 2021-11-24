"""
Operador ternário em python
"""

logado = True

msg = "usuário logado" if logado else "usuario precisa logar"

print(msg)

print("###########################################################################################################")

idade = input("Qual a sua idade: ")
if not idade.isnumeric():
    print("Voce precisa digitar apenas numeros")

else:
    idade = int(idade)
    maior_de_idade = (idade >= 18)
    msg = "É de maior " if maior_de_idade else "Não pode acessar o conteudo"

    print(msg)