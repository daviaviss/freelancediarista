from controladores.controlador_trabalho import ControladorTrabalho
from controladores.controlador_endereco import ControladorEndereco
from controladores.controlador_diarista import ControladorDiarista
from controladores.controlador_contratante import ControladorContratante
from controladores.controlador_pessoa import ControladorPessoa
from telas.tela_abstrata import *
from telas.tela_sistema  import TelaSistema

class ControladorSistema:
    def __init__(self):
        self.__controlador_contratante = ControladorContratante()
        self.__controlador_diarista = ControladorDiarista()
        self.__controlador_endereco = ControladorEndereco()
        self.__controlador_trabalho = ControladorTrabalho()
        self.__controlador_pessoa = ControladorPessoa()
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

    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa

    def inicializa_sistema(self):
        self.abre_tela_inicial()
   
    def encerra_programa(self):
        print("Programa Encerrado!")
        #self.tela_abstrata.mostra_mensagem("Programa Encerrado!")
        exit(0)

    def incluir_contratante(self):
        contratante = self.__controlador_pessoa.incluir_contratante()
        if contratante is not None:           
            self.abre_tela_inicial()
        else: 
            self.falha_email_ja_cadastrado()

    def incluir_diarista(self):
        diarista = self.__controlador_pessoa.incluir_diarista()
        if diarista is not None:           
            self.abre_tela_inicial()
        else: 
            self.falha_email_ja_cadastrado()    

    def abre_tela_inicial(self):
        lista_opcoes = {1: self.controla_tela_login, 2: self.incluir_usuario, 0: self.encerra_programa}
        opcao_escolhida = self.__tela_sistema.tela_inicial()
        lista_opcoes[opcao_escolhida]()

    def falha_email_ja_cadastrado(self):
        lista_opcoes = {1: self.controla_tela_login, 2: self.incluir_usuario, 0: self.encerra_programa}
        opcao_escolhida = self.__tela_sistema.tela_inicial()
        lista_opcoes[opcao_escolhida]()

    def controla_tela_login(self):
        lista_opcoes = {1:self.confere_login_contratante, 2:self.confere_login_diarista}
        opcao_escolhida = self.__tela_sistema.tela_login()

        if opcao_escolhida != 1 and opcao_escolhida != 2:
            print('A opção digitada é inválida, digite uma das opções dada!')
            self.controla_tela_login()
        
        else:
            lista_opcoes[opcao_escolhida]()

    def confere_login_contratante(self):
        contratante = self.__controlador_pessoas.confere_login(1)
        if contratante is not None:
            self.controla_menu_principal_contratante(contratante)  

    def confere_login_diarista(self):
        diarista = self.__controlador_pessoas.confere_login(2)
        if diarista is not None:
            self.controla_menu_principal_diarista(diarista)      

    def controla_menu_principal_contratante(self, usuario): #Arrumar
        lista_opcoes = {1: self.controla_produto_usuario, 2: self.controla_historico_usuario, 3: self.controla_pessoas_usuario, 4: self.inicializa_sistema}
        opcao_escolhida = self.__tela_sistema.tela_opcoes_usuario()
        if opcao_escolhida == 4:
            lista_opcoes[opcao_escolhida]()
        else:
            lista_opcoes[opcao_escolhida](usuario)    

    def controla_menu_principal_diarista(self, usuario): #Arrumar
        lista_opcoes = {1: self.controla_produto_usuario, 2: self.controla_historico_usuario, 3: self.controla_pessoas_usuario, 4: self.inicializa_sistema}
        opcao_escolhida = self.__tela_sistema.tela_opcoes_usuario()
        if opcao_escolhida == 4:
            lista_opcoes[opcao_escolhida]()
        else:
            lista_opcoes[opcao_escolhida](usuario)    