'''Faça um programa que pergunte o preço de três
   produtos e informe qual produto você deve comprar,
   sabendo que a decisão é sempre pelo mais barato. '''


produto1 = float(input('Insira o valor do produto 1: '))
produto2 = float(input('Insira o valor do produto 2: '))
produto3 = float(input('Insira o valor do produto 3: '))

if produto1 <= produto2 and produto1 <= produto3:
    menor = 'Produto 1'
elif produto2 <= produto1 and produto2 <= produto3:
    menor = "Produto 2"
else:
    menor = 'Produto 3'

print(f'\nMais barato: {menor}\n')