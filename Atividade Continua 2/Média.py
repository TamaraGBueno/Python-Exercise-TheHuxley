
#descreva um programa que receba as notas e a presença de um aluno, calcule a média e imprima a situação final do aluno.

#No semestre são feitas 3 provas, e faz-se a média ponderada com pesos 2, 2 e 3, respectivamente.

#Os critérios para aprovação são:

#1 - Frequência mínima de 75%.

#2 - Média final mínina de 6.0 (calculada com uma casa de precisão).

#E devem ser considerados os casos especiais descritos para a impressão dos resultados, com uma mensagem personalizada para cada situação.



p1 = float(input())
p2 = float(input())
p3 = float(input())
freq = float(input())
media = round((2*p1 + 2*p2 + 3*p3)/7,1)
porcentagem = int(freq*100)

print("Frequencia: {}%".format(porcentagem))
print("Media: {:.1f}".format(media))
if porcentagem < 75:
    print("Aluno reprovado por faltas!")
elif media > 9:
    print("Aluno aprovado com louvor!")
elif 6 <= media <= 9:
    print("Aluno aprovado!")
elif 4 <= media < 6:
    print("Aluno de recupera��o!")
else: 
    print("Aluno reprovado!")