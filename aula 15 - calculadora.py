while True:
    #declara as variaveis
    n1 = input("Digite n1: ")
    n2 = input("Digite n2: ")

    #verifica se as variaveis são numericas
    if not n1.isnumeric() or not n2.isnumeric():
        print("Voce precisa digitar um numero válido")
        continue

    #converte as variaveis para inteiro
    n1 = int(n1)
    n2 = int(n2)

    print("Operadores: + - * /")

    #pergunta o operador
    op = input("Digite um operador: ")

    #faz as operações abaixo
    if op == '+':
        print("{} + {} = {}" .format(n1, n2, n1 + n2))

    elif op == '-':
        print("{} + {} = {}".format(n1, n2, n1 - n2))

    elif op == '/':
        print("{} + {} = {}".format(n1, n2, n1 / n2))

    elif op == '*':
        print("{} + {} = {}".format(n1, n2, n1 * n2))

    #verifica se o usuário pretende sair do çaço
    sair = input("Deseja sair? [s] = sim / [n] = não ")

    if sair == 's':
        print("Até logo!!!")
        break
    else:
        continue