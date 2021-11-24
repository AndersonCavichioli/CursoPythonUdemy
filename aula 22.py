"""
troca de valores entre variáveis
"""

x = 10
y = "luiz"

x, y = y, x #x passa a receber o valor de y e y passa a receber o valor de x

print("x = {} e y = {}" .format(x, y))

a = "Tomate"
b = "Abacate"
c = "Melancia"

a, b, c = c, a, b

print("a = {} b = {} e c = {}".format( a, b, c))
