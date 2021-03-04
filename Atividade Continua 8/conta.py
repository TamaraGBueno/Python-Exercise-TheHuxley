# Linguagem de Programação II
# AC03 ADS-EaD - Módulos e importação
# arquivo: conta.py
# Prof. Rafael Maximo
#
# Email Impacta: tamara.bueno@aluno.faculdadeimpacta.com.br

from cliente import Cliente

class Conta:
    def __init__(self, clientes, numero_conta, saldo_inicial):
        self.__extrato = [('saldo inicial', saldo_inicial)]
        self.__clientes = clientes
        self.__numero = numero_conta
        self.__saldo = saldo_inicial

    def sacar(self, valor):
        if valor > self.__saldo:
            raise ValueError
        else:
            self.__extrato.append(('saque', valor))
            self.__saldo = self.__saldo-valor

    def depositar(self, valor):
        self.__extrato.append(('deposito', valor))
        self.__saldo = valor + self.__saldo

    def tirar_extrato(self):
        return self.__extrato

    @property
    def clientes(self):
        return self.__clientes

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo


