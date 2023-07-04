class Cadastro():
    def __init__(self, nome: str, descricao: str, pais: str, pesquisas: int) -> None:
        self.__nome = nome
        self.__descricao = descricao
        self.__pais = pais
        self.__pesquisas = pesquisas
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def pais(self):
        return self.__pais
    
    @property
    def pesquisas(self):
        return self.__pesquisas
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @pais.setter
    def pais(self, pais):
        self.__pais = pais

    @pesquisas.setter
    def pesquisas(self, pesquisas):
        self.__pesquisas = pesquisas

    def jsonificado(self):
        return {'nome': self.nome,
                'descricao': self.descricao,
                'pais': self.pais,
                'pesquisas': self.pesquisas}
