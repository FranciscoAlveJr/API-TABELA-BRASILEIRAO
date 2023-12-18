class Time:
    def __init__(self, nome, posicao, pontos, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, saldo_gols):
        self.__nome = nome
        self.__posicao = posicao
        self.__pontos = pontos
        self.__jogos = jogos
        self.__vitorias = vitorias
        self.__empates = empates
        self.__derrotas = derrotas
        self.__gols_pro = gols_pro
        self.__gols_contra = gols_contra
        self.__saldo_gols = saldo_gols

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def posicao(self):
        return self.__posicao
    
    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao

    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self, pontos):
        self.__pontos = pontos

    @property
    def jogos(self):
        return self.__jogos
    
    @jogos.setter
    def jogos(self, jogos):
        self.__jogos = jogos

    @property
    def vitorias(self):
        return self.__vitorias
    
    @vitorias.setter
    def vitorias(self, vitorias):
        self.__vitorias = vitorias

    @property
    def empates(self):
        return self.__empates
    
    @empates.setter
    def empates(self, empates):
        self.__empates = empates

    @property
    def derrotas(self):
        return self.__derrotas
    
    @derrotas.setter
    def derrotas(self, derrotas):
        self.__derrotas = derrotas

    @property
    def gols_pro(self):
        return self.__gols_pro
    
    @gols_pro.setter
    def gols_pro(self, gols_pro):
        self.__gols_pro = gols_pro

    @property
    def gols_contra(self):
        return self.__gols_contra
    
    @gols_contra.setter
    def gols_contra(self, gols_contra):
        self.__gols_contra = gols_contra

    @property
    def saldo_gols(self):
        return self.__saldo_gols
    
    @saldo_gols.setter
    def saldo_gols(self, saldo_gols):
        self.__saldo_gols = saldo_gols

        