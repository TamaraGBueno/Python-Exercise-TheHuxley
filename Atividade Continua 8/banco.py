# Linguagem de Programação II
# AC03 ADS-EaD - Módulos e importação
# arquivo: banco.py
# Prof. Rafael Maximo
#
# Email Impacta: tamara.bueno@aluno.faculdadeimpacta.com.br

# A classe Banco ira precisar da classe Conta, que deve ser importada aqui:
# sigam o exemplo dado na live 03, anexei os arquivos na postagem do Classroom.
# import conta ou from conta import Conta


from conta import Conta

class Banco:
    def __init__(self, nome):
        self.__nome = nome
        self.__contas = []
    

    def abre_conta(self, clientes, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError 
        else:
            num_contas = len(self.__contas)+1
            c1 = Conta(clientes, num_contas, saldo_inicial)
            self.__contas.append(c1)

    @property
    def nome(self):
        return self.__nome

    @property
    def contas(self):
        return self.__contas






