secreto = "perfume"
digitadas = [] # cria a lista vazia

print("Bem vindo ao jogo da forca!!")
print("Escolha uma dificuldade: \n 1 = fácil (5 chances) \n 2 = médio (4 chances) \n 3 = dificil (3 chances) \n")
escolha = int(input("E ai, qual será sua escolha? "))

if escolha == 1:
    chances = 5
elif escolha == 2:
    chances = 4
elif escolha == 3:
    chances = 3

print("Voce escolheu a opção: {} e tera {} chances de acertar!! Vamos começar: " .format(escolha, chances))

while True:
    if chances <= 0:
        print("Voce perdeu!!")
        print("A palavra secreta era: {}" .format(secreto))
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1: #verifica se foi digitado mais que 1 letra
        print("Digite apenas uma letra!!")
        continue # faz voltar ao inicio do laço

    digitadas.append(letra) # adiciona a letra digitada na lista

    if letra in secreto: # faz a verificação se a letra digitada contem na variavel secreta
        print("A letra {} existe na palavra secreta!" .format(letra))

    else:
        print("A letra {} não existe na palavra secreta" .format(letra))
        digitadas.pop() # faz a verificação se a letra digitada contem na variavel secreta e se nao estiver, remove da lista

    secreto_temporario = '' #cria uma variavel vazia

    for letra_secreta in secreto:

        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta

        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print("Voce descobriu a palavra secreta!! {}" .format(secreto))
        break

    else:
        print("A palavra secreta esta assim: {}" .format(secreto_temporario))

    if letra not in secreto:
        chances -= 1

    print("Voce ainda tem {} chances" .format(chances))
    print()
