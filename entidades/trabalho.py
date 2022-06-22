from entidades.contratante import Contratante
from entidades.endereco import Endereco

class Endereco:
    def __init__(self, contratante: Contratante, descricao: str, endereco: Endereco, salario: float):
        self.__contratante = contratante
        self.__descricao = descricao
        self.__endereco = endereco
        self.__salario = salario
        self.__disponibilidade = False

    @property
    def contratante(self):
        return self.__contratante

    @contratante.setter
    def contratante(self, contratante: Contratante):
        self.__contratante = contratante

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: Endereco):
        self.__endereco = endereco

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario: float):
        self.__salario = salario

    @property
    def disponibilidade(self):
        return self.__disponibilidade

    @disponibilidade.setter
    def disponibilidade(self, disponibilidade: bool):
        self.__disponibilidade = disponibilidade