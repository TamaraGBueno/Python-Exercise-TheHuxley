#Dados dois números inteiros A e B, exibir:

#- 'A eh maior', se A for maior do que B;

#- 'B eh maior', se B for maior do que A;

#- 'iguais', se os números forem iguais.



A = float(input())
B = float(input())

if A > B:
    print("A eh maior")
elif B > A:
    print("B eh maior")
else:
    print("iguais")
