import soma, mult, sub

num1 = int(input('Digite o primeiro valor '))
num2 = int(input('Digite o segundo valor '))

opcoes = int(input('Selecione sua opção \n 1 - Somar \n 2 - Subtrair \n 3 Multiplicar'))
if opcoes == 1:
    print(soma.Somar(num1, num2))
elif opcoes == 2:
    print(sub.Subtrair(num1, num2))
elif opcoes == 3:
    print(mult.Multiplicar(num1, num2))
else:
    print('Valor Inválido!')