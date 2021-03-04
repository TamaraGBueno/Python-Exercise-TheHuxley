#Você deve pedir que o usuário entre com um número inteiro, e deverá dizer se ele eh impar ou se ele eh par:

#Se ele for par imprima "O numero eh N e ele eh par"

#Se ele for impar imprima "O numero eh N e ele eh impar"

#Onde N eh o numero digitado pelo usuário





numero = int(input())
resto = numero%2
if resto == 0:
    print("O numero eh {} e ele eh par".format(numero))
else:
    print("O numero eh {} e ele eh impar".format(numero))
