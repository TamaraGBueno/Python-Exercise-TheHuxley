# Linguagem de Programação II
# AC01 ADS-EaD - Números Especiais
#
# Email Impacta: tamara.bueno@aluno.faculdadeimpacta.com.br


def eh_primo(n):
    var = n
    x = 1
    apoio = 0
    bol = False
    if var != 1:
        while x <= var:
            if (var%x) == 0:
                apoio = apoio+1
            else: 
                apoio = apoio
            x = x +1
    else: 
        apoio = 0
    if apoio == 2:
        bol = True
    else:
        bol = bol
    return bol
    pass


def lista_primos(n):
    a = []
    x = 1
    while x < n:
        if eh_primo(x) == True:
            a.append(x)
            x = x+1
        else:
            x = x+1
    return a
    pass


def eh_armstrong(n):
    soma = 0
    x = len(str(n))
    temp = n
    while temp > 0:
        digito = temp % 10
        soma += digito ** x
        temp //= 10
    return n == soma
    pass


def lista_armstrong(n):
    lista = []
    aux = n
    while aux >= 0:
        if eh_armstrong(aux) == True:
            lista.append(aux)
        else:
            pass
        aux = aux-1
    lista.sort()
    return lista
    pass


def eh_perfeito(n):
    soma = 0
    for x in range(1, n):
        if n % x == 0:
            soma+= x
    return soma == n
    pass


def lista_perfeitos(n):
    lista = []
    aux = n
    while aux > 0:
        if eh_perfeito(aux) == True:
            lista.append(aux)
        else:
            pass
        aux = aux-1
    lista.sort()
    return lista
    pass
