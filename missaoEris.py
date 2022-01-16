'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
 
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
    entre 3 e 4 como "Cúmplice",
    5 como "Assassino".
    Caso contrário, ele será classificado como "Inocente".
'''


print('\n----- Interrogatório -----\n')
print('Responda as seguintes perguntas com S para sim ou N para não\n\n')
soma = 0
q1 = input('1 - Telefonou para a vítima? ')
if q1.lower() == 's':
    soma += 1
q2 = input('2 - Esteve no local do crime? ')
if q2.lower() == 's':
    soma += 1
q3 = input("3 - Mora perto da vítima? ")
if q3.lower == 's':
    soma += 1
q4 = input("4 - Devia para a vítima? ")
if q4.lower == 's':
    soma += 1
q5 = input("5 - Já trabalhou com a vítima? ")
if q5.lower == 's':
    soma += 1
print('\n')
if soma == 2:
    print('Suspeito\n')
elif soma > 2 and soma < 5:
    print('Cumplice\n')
elif soma == 5:
    print('Assassino\n')
else:
    print('Inocente\n')