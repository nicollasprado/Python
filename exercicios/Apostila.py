# 2.6
# Questao 1
x = 10+3*3
print("Q.1=", type(x), x)
# resultado 19 e tipo inteiro

# Q.2
x = 10+18/2
print("Q.2", type(x), x)
# resultado 19.0 e tipo real

# Q.3
x = 10+18//2-1
print("Q.3=", type(x), x)
# resultado 18 e tipo inteiro

# Q.4
x = 1+2*3+40//3%5-2+3*5%2
print("Q.4=", type(x), x)
# O resultado é 9 e é um inteiro pois foi realizada uma divisão inteira

# Q.5
x = 1+2*3+40/3%5-2+3//2*5
print("Q.5=", type(x), x)
# O resultado é 13.333... e é um numero real pois foi realizada uma divisão real

# Q.6
soma = 0
x = 0

while soma < 10:
    soma = soma+1
    x = x+soma
    if soma == 10:
        print("Q.6=", x)
        break
# Resultado equivale a 55

# Q.7
valores = [7, 7, 8, 35]
conta = 0

for item in valores:
    conta = conta+item
print("Q.7=", conta)
# Resultado igual a 57

# Q.8
n1 = 5.2
n2 = 8.2
peso1 = 2
peso2 = 3
media_final = (n1*peso1 + n2*peso2)/(peso1+peso2)
print("Q.8=", media_final)
# Resultado equivale a 7.0

# Q.9 Em desenvolvimento!!
x = str(input("Digite um valor "))
quantidade_digitos = len(x)
contador = int(0)
qtd_zeros = "1"
print("QTD digitos=", quantidade_digitos)
while contador < quantidade_digitos-1:
    contador = contador+1
    qtd_zeros = qtd_zeros+"0"
    print(contador)
    if contador == quantidade_digitos:
        qtd_zeros_int = int(qtd_zeros)
        x_int = int(x)
        print("Dados:", x_int, qtd_zeros_int)
        print("Resltado:", x_int/qtd_zeros_int)
        break
        