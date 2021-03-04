# Linguagem de Programação II
# AC03 ADS-EaD - Módulos e importação
# arquivo: cliente.py
# Prof. Rafael Maximo
#
# Email Impacta: tamara.bueno@aluno.faculdadeimpacta.com.br



class Cliente:
    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.telefone = telefone
        self.email = email

    @property
    def nome(self):
       return self.__nome
       

    @property
    def telefone(self):
        return self.__telefone
        

    @telefone.setter
    def telefone(self, novo_telefone):
        if not isinstance(novo_telefone, int):
            raise TypeError
        self.__telefone = novo_telefone
   

    @property
    def email(self):
       return self.__email
        
    @email.setter
    def email(self, novo_email):
        if not isinstance(novo_email, str):
            raise TypeError
        elif '@' not in novo_email:
            raise ValueError 
        else:
            self.__email = novo_email



    