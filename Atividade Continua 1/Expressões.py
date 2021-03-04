#Escreva um programa em Python3 que receba quatro números reais (a, b, c, d) e reproduza as seguintes expressões algébricas:

#DICA 1: A única função que vocês precisam usar do módulo de mátemática é a função log (ou log10).

#DICA 2: Usem os valores do número Pi e do Número de Euler (e) também do módulo de matemática.

#DICA 3: Não existe (até onde eu sei) uma função para calcular a raiz cúbica no Python, e isso tampouco é necessário, pois toda e qualquer raiz pode ser reescrita como um expoente fracionário.

#Formato de entrada

#As entradas poderão ser quaisquer números reais, positivos ou negativos mas não nulos.

#Não imprima nenhum texto para pedir os dados de entrada.

#Formato de saída

#Durante o cálculo, o valor final calculado para cada item deve ser arredondado para 4 casas decimais, usando a função round.:

#round(n, d)

#Que retorna o valor de n arredondado para d casas após a vírgula. Se d for omitido, é feito o arredondamento para um número inteiro.
#Obs.: Essa função não faz parte do módulo de matemática, podendo ser acessada diretamente.


#Para este exercício, não deve ser feita a formatação do número para 4 casas decimais na construção da string, ou seja, não use o {:.4f} (ou variantes) pois isso irá completar com zeros o valor até a quarta casa:

#Correto:
#>>> print(round(3.599999999, 4))
#3.6
#Incorreto (para este exercício):
#>>> print('{:.4f}'.format(3.599999999))
#3.6000



a = float(input())
b = float(input())
c = float(input())
d = float(input())
import math

i = ((a**2)+3*b)/c+d
ii = math.log10(a)+((math.e)**(-b/c))-(d**2)/math.pi
iii = ((a**(2/3))*(b**(1/3))+(c*d))/(a+b+c+d)
iv = ((a+b)*(c+d))/(a*b*c*d)
v = (((a**2)+(b**2))/(c*d))-(((c**2)+(d**2))/(a*b))
vi = (a+b+c+d)**2
vii = (a**2+b**2+c**2+d**2)
viii = ((a*b*c*d)**(1/3))

print("i)",round(i,4))
print("ii)",round(ii,4))
print("iii)",round(iii,4))
print("iv)",round(iv,4))
print("v)",round(v,4))
print("vi)",round(vi,4))
print("vii)",round(vii,4))
print("viii)",round(viii,4))