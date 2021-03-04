#Faça um programa que leia um número inteiro e imprima a tabuada de multiplicação deste número. Suponha que o número lido da entrada é maior que zero.


cont = 1
numero = int(input())
while cont<=9:
    print(numero, "X", cont, "=", numero * cont)
    cont = cont+1