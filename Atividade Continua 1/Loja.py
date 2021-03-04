
#Imagine que você fora contratado para fazer um programa para uma loja de tintas, com o objetivo de calcular quantas latas de tinta são necessárias para pintar uma determinada área e calcular o preço final da compra.

#A loja trabalha com latas de tinta de:
#24 litros, vendidas a R$91,00 cada e,
#5.4 litros, vendidas a R$23,00 cada.
#Sabe-se ainda que cada litro de tinta cobre uma superfície de 7 metros quadrados.

#Faça um programa que receba o valor da área a ser pintada em metros quadrados, calcule e imprima:

#a) A quantidade de latas de tinta e o preço final, considerando apenas latas de 24 litros.
#b) A quantidade de latas de tinta e o preço final, considerando apenas latas de 5.4 litros.
#c) A quantidade de latas de tinta e o preço final, considerando ambas as latas, de 24 e 5.4 litros.



import math

area = float(input())
quantidade = float(area/7)

latasgrandes1 = math.ceil(float(quantidade/24))
latasgrandes2 = math.floor(float(quantidade/24))
lataspequenas1 = math.ceil(float(quantidade/5.4))

print("a)",latasgrandes1,"lata(s) de 24 litros: R$ {:.2f}".format(latasgrandes1*91.00))
print("b)",lataspequenas1,"lata(s) de 5.4 litros: R$ {:.2f}".format(lataspequenas1*23.00))

if(latasgrandes2 > 0):
    sobras = quantidade-(latasgrandes2*24)
    sobraspequenas = math.ceil(float(sobras/5.4))
    print("c)",latasgrandes2,"lata(s) de 24 litros e",sobraspequenas,"lata(s) de 5.4 litros: R$ {:.2f}".format((latasgrandes2*91.00 + sobraspequenas*23.00)))
else: print("c)",0,"lata(s) de 24 litros e",lataspequenas1,"lata(s) de 5.4 litros: R$ {:.2f}".format(float(lataspequenas1*23.00)))