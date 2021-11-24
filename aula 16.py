"""
for in python
iterando strings com python
"""
texto = "Alguma coisa escrita aqui"

for n, a in enumerate(texto): # joga a enumeração na variavel a
    print(n, a)

for n in range(0, len(texto)): # pegando todas as posições da variavel texto
    print(n)

for n in range(0, len(texto), 2): # pula de 2 em 2
    print(n)

nova_string = ''

for letra in texto:
    if letra == 'c':
        nova_string = nova_string + letra.upper()
    else:
        nova_string += letra

print(nova_string)
