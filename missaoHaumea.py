'''Escreva um programa  para converter um número decimal em número octal.
Dados de teste:
Insira um número decimal: 15
Resultado esperado:
O número octal é: 17
'''
print('\n\n###### CONVERSOR DE DECIMAL PARA OCTAL ######\n')
num = int(input('\nInsira um número decimal: '))
resposta = oct(num)
print(f'\nO numero octal é: {resposta[2:]}\n')