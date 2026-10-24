# EXERCÍCIO: CAIXA ELETRÔNICO
#
# Crie um programa em Python que simule uma operação de saque
# em um caixa eletrônico.
#
# O programa deverá solicitar ao usuário o saldo disponível
# em sua conta e o valor que deseja sacar.
#
# Verifique se a operação pode ser realizada e apresente
# uma mensagem correspondente à situação encontrada.

saldo = float(input('Qual o saldo da conta? '))
saque = float(input('Qual o valor que você deseja sacar? '))
if saldo <=0:
    print('O VALOR É INVALIDO')

elif saque <= 0:
    print('O VALOR É INVALIDO')

elif saque > saldo:
    print('O SALDO É INSUFICIENTE')

else:
    restante = saldo - saque
    print('O SAQUE FOI REALIZADO')
    print(f'O restante que sobrou na conta foi de {restante:.2f}')