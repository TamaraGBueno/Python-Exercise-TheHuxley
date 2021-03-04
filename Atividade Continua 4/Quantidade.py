#Crie um programa que tenha uma única função, além da principal, que receberá como parâmetro uma string não vazia s (com no máximo 50 caracteres de conteúdo) e exibirá a quantidade de caracteres de s. Observações: (a) apenas um laço de repetição; (b) sem matrizes auxiliares; (c) não usar funções prontas; (d) função iterativa.


svalido = False

while svalido == False:
  s= str(input())
  l = len(s)
  if 0 < l <= 50:
    svalido = True
    print(l)
  else:
    svalido = False
