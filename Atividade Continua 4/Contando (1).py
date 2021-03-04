#Escreva um programa que irá receber duas entradas: uma sequencia de caracteres e um único caractere e irá contar quantas vezes o caractere aparece na sequencia. Você deve escrever uma função que irá receber como parâmetros a sequencia e o caractere, e retornar o número de ocorrências pedido. No código principal do programa, faça a leitura dos dados de entrada (input's), chame a sua função para contar o número de ocorrências, e em seguida imprima o resultado pedido.

#OBS: Não é permitido o uso do .count() para realizar a contagem.



x1 = input()
x2 = input()
z = 0

if x2 not in x1:
    print("Caractere nao encontrado.")
else:
    x = x1.split(x2)
    for y in x:
        z += 1

    print("O caractere buscado ocorre",(z-1),"vezes na sequencia.")