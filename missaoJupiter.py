'''Escreva um programa para converter segundos em horas, minutos e segundos. 
Dados de teste:
Segundos de entrada: 86399 
Resultado esperado:
Saída de amostra: 23:59:59
'''

def conversao(segundosEntrada):
    horas = segundosEntrada//3600
    minutos = (segundosEntrada%3600)//60
    segundos = (segundosEntrada%3600)%60
    print(f'{horas}:{minutos}:{segundos}')
    

if __name__ == '__main__':
    segundosEntrada = int(input('\nSegundos de entrada: '))
    conversao(segundosEntrada)
    print('\n')