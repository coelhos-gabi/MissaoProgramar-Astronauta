'''Escreva um programa para reverter uma string. (Opcional : faça se vc souber usar array(“vetor”))
Dados de teste:
The quick brown fox
Resultado esperado:
String reversa: xof nworb kciuq ehT
'''

string = input('Insira uma frase: ')
for n in range(1,len(string)+1):
    print(string[-n], end='')