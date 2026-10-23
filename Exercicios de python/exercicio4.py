# ==========================================
# DESAFIO: CALCULADORA DE IMC
# NÍVEL: INTERMEDIÁRIO
# ASSUNTO: IF, ELIF, ELSE E OPERADORES LÓGICOS
# ==========================================

# OBJETIVO:
# Desenvolva um programa que calcule o Índice de
# Massa Corporal (IMC) de uma pessoa e apresente
# uma classificação de acordo com o resultado.

# ENTRADA DE DADOS:
# Solicite ao usuário seu peso em quilogramas
# e sua altura em metros.
#
# Os valores digitados podem conter casas decimais.

# PROCESSAMENTO:
# Utilize os dados informados para calcular o IMC.
#
# A fórmula matemática deverá ser aplicada corretamente.

# VALIDAÇÃO:
# O programa deverá verificar se os dados informados
# são válidos antes de realizar o cálculo.
#
# Caso os dados sejam inválidos, apresente uma
# mensagem de erro apropriada e não continue o cálculo.

# CLASSIFICAÇÃO:
# Depois de calcular o IMC, o programa deverá
# identificar a classificação correspondente.
#
# Considere as seguintes categorias para adultos:
# - Abaixo do peso
# - Peso normal
# - Sobrepeso
# - Obesidade grau I
# - Obesidade grau II
# - Obesidade grau III
#
# Pesquise ou consulte os limites de cada categoria
# e implemente as condições necessárias.

# SAÍDA:
# Apresente o resultado do IMC com duas casas decimais.
# Em seguida, mostre a classificação correspondente.


peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

if altura <= 0 or peso <= 0:
    print('ERRO, A ALTURA E NEM O PESO PODE SER 0')

else:
    imc = peso / (altura * altura)
    print(f'Seu IMC é de {imc:.2f}')

    if imc < 18.5:
        print('Você esta abaixo do peso!!!')

    elif imc >= 18.5 and imc < 25:
        print('Peso normal')

    elif imc >= 25 and imc < 30:
        print('Você esta com sobrepeso!!!')

    elif imc >= 30 and imc < 35:
        print('Você esta com obesidade grau 1 !!!')

    elif imc >= 35 and imc < 40:
        print('Você esta com obesidade grau 2 !!!')

    else:
        print('Você esta com obesidade grau III')