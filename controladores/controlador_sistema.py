from controladores.controlador_trabalho import ControladorTrabalho
from controladores.controlador_endereco import ControladorEndereco
from controladores.controlador_diarista import ControladorDiarista
from controladores.controlador_contratante import ControladorContratante
from telas.tela_abstrata import *
from telas.tela_sistema  import TelaSistema

class ControladorSistema:
    def __init__(self):
        self.__controlador_contratante = ControladorContratante()
        self.__controlador_diarista = ControladorDiarista()
        self.__controlador_endereco = ControladorEndereco()
        self.__controlador_trabalho = ControladorTrabalho()
        self.__tela_sistema = TelaSistema()


    @property
    def controlador_contratante(self):
        return self.__controlador_contratante

    @property
    def controlador_diarista(self):
        return self.__controlador_diarista

    @property
    def controlador_endereco(self):
        return self.__controlador_endereco

    @property
    def controlador_trabalho(self):
        return self.__controlador_trabalho

    def inicializa_sistema(self):
        self.abre_tela_inicial()
   
    def encerra_programa(self):
        self.tela_abstrata.mostra_mensagem("Programa Encerrado!")
        exit(0)

    def fazer_login(self):
        pass

    def cadastrar_usuario(self):
        pass

    def abre_tela_inicial(self):
        lista_opcoes = {1: self.fazer_login, 2: self.cadastrar_usuario, 0: self.encerra_programa}
        opcao_escolhida = self.__tela_sistema.tela_inicial()
        lista_opcoes[opcao_escolhida]()
