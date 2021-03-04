#Faça um programa que receba dois inteiros x e n, com x, n > 0 e x < n, e conte o número de múltplos de x menores do que n.

#DICA 1: Os múltiplos de um número são obtidos multiplicando-se esse número pelos números naturais (1, 2, 3, 4, 5, ...)

#DICA 2: No primeiro exemplo, os múltiplos de são: 7*1, 7*2, 7*3, 7*4, 7*5, .... --> 7, 14, 21, 28, 35, ... Sendo assim, temos 3 múltiplos que são estritamente menores que 28, já que o quarto múltiplo é o próprio 28 (portanto = e não < ).

#DICA 3: Use um laço de repetição para ir percorrendo os números inteiros e um acumulador para contar +1 para cada múltiplo encontrado, parando quando o múltiplo da vez for igual ao número limite dado (ou seja, deve executar enquando ele for menor).



n = int(input())
nlimite = int(input())
contador = 0

for x in range (n,nlimite, n):
  if x < nlimite:
    contador = contador + 1
  else: break
print("O numero {} tem {} multiplos menores que {}.".format(n,contador,nlimite))
            
