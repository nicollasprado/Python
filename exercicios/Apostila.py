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
# O resultado é 13.333... e é um numero real pois foi realizada uma divisão entre numeros inteiros que resultou em um valor quebrado

# Q.6
contador = 0
x = 0

while contador < 10:
    contador = contador+1
    x = x+contador
    if contador == 10:
        print("Q.6=", x)
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
media_final = (n1 * peso1 + n2 * peso2) / (peso1 + peso2)
print("Q.8=", media_final)
# Resultado equivale a 7.0

# Q.9
x = str(input("Digite um valor "))
tamanho_x = len(x)
zeros = ''
for contador in range(tamanho_x-1): # Determinando a quantidade de zeros
    zero = str(tamanho_x % tamanho_x)
    zeros = zeros + zero
divisor = str('1' + str(zeros))
ultimo_digito = int(x) % int(divisor)
print('Q.9=', ultimo_digito)

# x = 73623
# ultimo_digito = x % 10
# print('ULTIMO DIGITO:', ultimo_digito)

# Q.10
tempoTOT = int(input('Digite um valor em segundos '))
seg = 0

while seg < tempoTOT:
    seg = seg+1
    if seg == tempoTOT:
        m = seg/60
        h = seg/3600
        print('Q10 Segundos:', seg)
        print('Q10 Minutos:', m)
        print('Q10 Horas:', h)

# Q.11
x = str(input('Digite um número de 4 digitos '))
qtd_digitos = len(x)
if qtd_digitos != 4:
    print('ERRO: O número não tem 4 digitos')
else:
 x_invertido = ''
 for contador in range(qtd_digitos):
    num_da_vez = x[contador]
    num_final = int(num_da_vez) % 10
    x_invertido = str(num_final) + x_invertido
 print(int(x_invertido))