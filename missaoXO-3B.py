'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 
Dados de teste:
Insira uma letra: A
Resultado esperado:
A letra é : Vogal
'''

letra = input('Insira uma letra: ')
string = letra.lower()

if string == 'a'or string == 'e'or string == 'i'or string == 'o'or string == 'u':
    print(f'A letra é:')