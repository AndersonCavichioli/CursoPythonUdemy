nome = "teste de string"

print(nome.lower()) # tudo minusculo
print(nome.upper()) # tudo maiusculo
print(nome.title()) # primeira letra maiuscula de cada palavra

texto = 'um texto qualquer aqui dentro'

print(texto[0]) # pega o caractere da posição 0 da string
print(texto[0:3]) # pega os index da posição 0 ate a posição 3
print(texto[:-1]) # tira a ultima letra da string

nova_string = texto[2:6] #criou uma string com os caracteres entre a posição 2 e 6
print(nova_string)

print(texto[0::2]) # vai ate o ultimo caractere pulando de 2 em 2

