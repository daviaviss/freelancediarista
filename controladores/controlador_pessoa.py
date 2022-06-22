from entidades.contratante import Contratante
from entidades.diarista import Diarista
from telas.tela_pessoa import TelaPessoa
from telas.tela_abstrata import *

class ControladorPessoa():
    
    def __init__(self, controlador_sistema):
        self.__contratantes = []
        self.__diaristas = []
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_sistema = controlador_sistema

    def incluir_contratante(self):
        dados_novo_contratante = self.__tela_contratante.pega_dados_contratante()
        contratante_nome = self.confere_contratante_nome(dados_novo_contratante["nome"])
        contratante_telefone = self.confere_contratante_telefone(dados_novo_contratante["telefone"])
        if contratante_nome == None and contratante_nome == None:
            novo_contratante = Contratante(dados_novo_contratante["nome"], dados_novo_contratante["telefone"])
            self.__contratantes.append(novo_contratante)
            print('Seu cadastro foi realizado com sucesso!')
            return novo_contratante
        else:
            print('ATENÇÃO: O Nome ou o e-mail informados já estão cadastrados!')
            return None

    def incluir_diarista(self):
        dados_nova_diarista = self.__tela_diarista.pega_dados_diarista()
        diarista_nome = self.confere_diarista_nome(dados_nova_diarista["nome"])
        diarista_telefone = self.confere_diarista_telefone(dados_nova_diarista["telefone"])
        if diarista_nome == None and diarista_nome == None:
            nova_diarista = Diarista(dados_nova_diarista["nome"], dados_nova_diarista["telefone"])
            self.__diaristas.append(nova_diarista)
            print('Seu cadastro foi realizado com sucesso!')
            return nova_diarista
        else:
            print('ATENÇÃO: O Nome ou o e-mail informados já estão cadastrados!')
            return None         