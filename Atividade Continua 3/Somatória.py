#Escreva um programa em Python 3 que receba dois números inteiros representando uma progressão aritmética começando sempre em 1 e calcule a sua somatória.

#O primeiro é a razão R da PA e o segundo é o último número N da série.

#Exemplo: R = 3 e N = 22 resulta na seguinte série: 1, 4, 7, 10, 13, 16, 19, 22





razao = int(input())
n = int(input()) 
n1 = n+1
soma_razao = 0

for c in range (1, n1 , razao):
    soma_razao += c
 
print("A somatoria da PA eh: {}".format(soma_razao))


