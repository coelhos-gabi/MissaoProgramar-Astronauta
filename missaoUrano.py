'''Escreva um programa  que recebe um número como entrada e imprime sua tabuada até 10.  
Dica: #Estrutura de repetição
Dados de teste:
Insira um número: 8
'''
def tabuada(a):
    for n in range(11):
        print(f'{a} x {n} = {a * n}')

if __name__ == '__main__':
    print('----------')
    print(' Tabuada')
    print('----------')
    a = int (input('\nInsira um número: '))
    tabuada(a)
    print("\n")
