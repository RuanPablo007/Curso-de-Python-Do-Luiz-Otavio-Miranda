# EXERCÍCIO 2 - CLASSIFICADOR DE IDADE
# Crie um programa que solicite a idade do usuário.
# Se a idade for menor que 0, exiba "Idade inválida".
# Se a idade for menor que 12, exiba "Criança".
# Se a idade estiver entre 12 e 17 anos, exiba "Adolescente".
# Se a idade estiver entre 18 e 59 anos, exiba "Adulto".
# Se a idade for maior ou igual a 60, exiba "Idoso".
# Utilize if, elif e else para resolver o exercício.


idade = int(input('Qual sua idade? '))

if idade < 12:
    print('Você é uma criança')
elif idade >= 12 and idade <= 17:
    print('Você é um adolescente')
elif idade >= 18 and idade <= 59:
    print('Você é um adulto')
else:
    print('Você é um idoso')
