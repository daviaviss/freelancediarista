class Endereco:
    def __init__(self, cidade: str, bairro: str, rua: str, numero: int):
        self.__cidade = cidade
        self.__bairro = bairro
        self.__rua = rua
        self.__numero = numero

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = cidade

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro: str):
        self.__bairro = bairro

    @property
    def rua(self):
        return self.__rua

    @rua.setter
    def rua(self, rua: str):
        self.__rua = rua

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero