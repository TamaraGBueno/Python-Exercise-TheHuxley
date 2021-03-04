#Faça um programa de resolução de tabuada. O programa deve inicialmente receber 2 números que indicam de quais números devem ser impressas a tabuada. Por exemplo, se forem recebidos os valores 2 e 5, seu programa deve imprimir a tabuada de 2, 3, 4 e 5. O programa só deve aceitar valores entre 1 e 9. Enquanto o usuário digitar valores que não sejam esses, emita uma mensagem de erro.




v1valido = False
v2valido = False
while v1valido == False:
  v1= int(input())
  if 1 <= v1 <= 9:
    v1valido = True
  else:
    print("Insira um n�mero inicial entre 1 e 9")
    v1valido = False
while v2valido == False:
  v2 = int(input())
  if 1 <= v2 <= 9:
    v2valido = True
  else:
    print("Insira um n�mero final entre 1 e 9")      
    v2valido = False
contv1 = v1
if v1 <= v2:
  while contv1 <= v2:
    cont = 1  
    while cont<=9:
      print(contv1, "x", cont, "=", contv1 * cont)
      cont = cont+1
    print("")
    contv1=contv1+1
    
else:
  print("Nenhuma tabuada nesse intervalo")