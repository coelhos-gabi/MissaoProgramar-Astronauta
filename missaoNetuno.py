'''
Escreva um programa  para aceitar um número e verifique se o número é par ou não.
Imprime 1 se o número for par ou 0 se o número for ímpar. 
Dica: #Estrutura de decisão
Dados de teste:
Insira um número: 20
Resultado esperado:
Saída de amostra: 1
'''

def par(a):
    if a % 2 == 0:
        return 1
    else:
        return 0

if __name__ == "__main__":
    a = float(input('Insira um número: '))
    print(par(a))