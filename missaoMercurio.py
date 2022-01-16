'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contaram para desenvolver o programa que calculará os reajustes. 
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.

'''
print('\n---------- CALCULE O REAJUSTE ----------\n\n')
salario = float(input("Insira o salário: "))
p1 = 0.20
p2 = 0.15
p3 = 0.10
p4 = 0.05

if salario <= 280:
    porcentagem = p1
    novoSalario = salario * (1 + porcentagem)
elif 280 < salario <= 700:
    porcentagem = p2
    novoSalario = salario*(1 + porcentagem)
elif 700 < salario <= 1500:
    porcentagem = p3
    novoSalario = salario*(1 + porcentagem)
else:
    porcentagem = p4
    novoSalario = salario*(1 + porcentagem)
aumento = novoSalario-salario

print(
    f'\n\nSalario antes do reasjute: {salario}\nPercentual de aumento: {porcentagem*100}%\nValor do aumento: {round(aumento,2)}\nNovo salario: {round(novoSalario,2)}\n\n')
