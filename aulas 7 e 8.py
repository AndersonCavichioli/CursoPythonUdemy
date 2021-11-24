import datetime #importa a biblioteca datetime

nome = "Anderson"
idade = 30
altura = 1.80
e_maior = idade > 18
peso = 80


imc = peso / (altura * altura) #calcula o IMC 

#Pega a data atual e retira apenas o ano
dt = datetime.datetime.now()
data = dt.date()
year = int(data.strftime("%Y"))

nasc = year - idade

print("Ola, meu nome é {}, tenho {} anos, {} de altura e peso {}kg" .format(nome, idade, altura, peso))
print("O IMC de {} é {:.2f}" .format(nome, imc))
print("{} nasceu em {}" .format(nome, nasc))

