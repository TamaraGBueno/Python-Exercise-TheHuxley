# Linguagem de Programação II
# AC02 ADS-EaD - Classes e Herança
# Prof. Rafael Maximo
#
# Email Impacta: tamara.bueno@aluno.faculdadeimpacta.com.br

# ------------------ #
# Criando uma classe #
# ------------------ #

# Crie a classe Mamifero seguindo o exemplo da classe Reptil
# Para esta AC não utilizem o @property ainda


class Reptil:
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def tomar_sol(self):
        return '{} tomando sol'.format(self.nome)

    def botar_ovo(self):
        if self.idade > 2:
            return '{} botou um ovo'.format(self.nome)
        else:
            return '{} ainda não atingiu maturidade sexual'.format(self.nome)


class Mamifero:
    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.idade = idade
        self.tipo_pata = tipo_pata

    def correr(self):
        return "{} correndo".format(self.nome)

    def mamar(self):
        if self.idade <=1:
            return "{} mamando".format(self.nome)
        else:
            return "{} já desmamou".format(self.nome)
            

# ------------------------- #
# Criando as classes filhas #
# ------------------------- #

# Crie as classes filhas Cavalo, Cachoro, Gato, Cobra e Jacaré
# seguindo o exemplo da classe Camaleao abaixo
# Para esta AC não utilizem o @property ainda

class Camaleao(Reptil):
    def __init__(self, nome, cor, idade, inseto_favorito):
        super().__init__(nome, cor, idade)
        self.inseto_favorito = inseto_favorito

    def mudar_de_cor(self):
        return '{} mudando de cor'.format(self.nome)

    def comer_inseto(self):
        return '{} comendo inseto'.format(self.nome)



class Cavalo(Mamifero):

    def __init__(self, nome, cor_pelo, idade, tipo_pata, cor_crina):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.cor_crina = cor_crina

    def galopar(self):
        return "{} galopando".format(self.nome)

    def relinchar(self):
        return "{} relinchando".format(self.nome)



class Cachorro(Mamifero):
   
    def __init__(self, nome, cor_pelo, idade, tipo_pata, raca):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.raca = raca


    def latir(self):
        return "{} latindo".format(self.nome)
    

    def rosnar(self):
        return "{} rosnando".format(self.nome)


class Gato(Mamifero):
   
    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.vidas = 7

    def miar(self):
        return '{} miando'.format(self.nome)
    
    def morrer(self):
        self.vidas = self.vidas-1
        if self.vidas <= 0:
            return '{} morreu'.format(self.nome)
        else:
            return '{} tem {} vidas sobrando'.format(self.nome,self.vidas)


class Cobra(Reptil):
   
    def __init__(self, nome, cor, idade, veneno):
        super().__init__(nome, cor, idade)
        self.veneno = veneno
        
    def rastejar(self):
        return '{} rastejando'.format(self.nome)

    def trocar_pele(self):
        return '{} trocando de pele'.format(self.nome)


class Jacare(Reptil):
   
    def __init__(self, nome, cor, idade, num_dentes):
        super().__init__(nome, cor, idade)
        self.num_dentes = num_dentes

    def atacar(self):
        return '{} atacando'.format(self.nome)

    def dormir(self):
        return '{} dormindo'.format(self.nome)