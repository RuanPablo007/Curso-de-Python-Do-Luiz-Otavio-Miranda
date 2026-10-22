# EXERCÍCIO 1 - SISTEMA DE NOTAS
# Crie um programa que solicite quatro notas ao usuário e calcule a média.
# Se a média for maior ou igual a 7, exiba "Aprovado".
# Se a média for maior ou igual a 5 e menor que 7, exiba "Recuperação".
# Caso contrário, exiba "Reprovado".

nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi sua segunda nota? '))
nota3 = float(input('Qual foi sua terceira nota? '))
nota4 = float(input('Qual foi sua quarta nota? '))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print('Você foi aprovado, PARABENS!!!')
elif media >= 5:
    print('Você esta de recuperação!!!')
else:
    print('Você foi reprovado!')