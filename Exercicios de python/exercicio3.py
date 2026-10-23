# DESAFIO: Corrija os erros deste programa.
# O programa deve receber a idade de uma pessoa
# e informar se ela é criança, adolescente, adulta ou idosa.
#
# Regras:
# Menor que 12 anos: criança
# De 12 até 17 anos: adolescente
# De 18 até 59 anos: adulto
# 60 anos ou mais: idoso
#
# ATENÇÃO: O código já está pronto, mas possui erros de lógica.
# Encontre e corrija os erros sem mudar as regras do programa.

'''
CODIGO ANTES DA CORREÇÃO:
idade = int(input('Digite sua idade: '))

if idade > 12:
    print('Você é uma criança')

elif idade >= 12 and idade < 17:
    print('Você é um adolescente')

elif idade >= 18 and idade <= 59:
    print('Você é um adulto')

elif idade < 60:
    print('Você é um idoso')

else:
    print('Idade inválida')
'''

# CODIGO APÓS CORREÇÃO:
idade = int(input('Digite sua idade: '))
if idade < 12 and idade >= 1:
    print('Você é uma criança')
elif idade >= 12 and idade <= 17:
    print('Você é um adolescente')
elif idade >= 18 and idade <= 59:
    print('Você é um adulto')
elif idade >= 60:
    print('Você é um idoso')
else:
    print('Idade inválida')