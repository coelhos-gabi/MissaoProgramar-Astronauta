def dividir(a,b):
    return int(a/b)



if __name__ == "__main__":
    divisao = input('Insira a divisao: ')
    num = divisao.split('/')
    a = float(num[0])
    b = float(num[1])
    print(dividir(a,b))