x = int(input('Digite o primeiro valor '))
y = int(input('Digite o segundo valor '))

def calcular (valor1, valor2):
    valor1 += 10
    valor2 += 5
    print('Valor 1: {}; Valor 2: {}'.format(valor1, valor2))
calcular(x, y)