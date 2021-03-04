#Escreva um programa em Python3 que receba um número real positivo e não nulo, calcule e imprima o resultado das seguintes operações aritméticas (n é o número recebido e e é o número de Euler):

#DICA 1: A única função que vocês precisam usar do módulo de mátemática é a função log.

#DICA 2: Usem os valores do número Pi e do Número de Euler (e) também do módulo de matemática.

#DICA 3: Não existe (até onde eu sei) uma função para calcular a raiz cúbica no Python, e isso tampouco é necessário, pois toda e qualquer raiz pode ser reescrita como um expoente fracionário. nts>Texto<a>

#Formato de entrada

#A entrada será um número real positivo e não nulo. Não imprima nenhum texto para pedir o dado de entrada.

#Formato de saída

#A saída devera conter a resposta de cada item em uma linha diferente, contendo apenas o número do item e o valor calculado, sem formatação nem arredondamento


n = float(input())

import math

i = n**2
ii = n**math.e
iii = n**(1/2)
iv = n**(1/3)
v = n**(1/n)
vi = math.e*n
vii = math.pi/n
viii = math.log(n,7)
ix = math.log(n,math.e)
x = math.log(n,math.pi)

print('i)',i)
print('ii)',ii)
print('iii)',iii)
print('iv)',iv)
print('v)',v)
print('vi)',vi)
print('vii)',vii)
print('viii)',viii)
print('ix)',ix)
print('x)',x)
