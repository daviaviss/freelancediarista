from telas.tela_abstrata import *

class TelaPessoa:

    def pega_dados_diarista_contratante(self):

        cabecalho('Insira os dados abaixo')

        nome = input("Nome: ")
        telefone = input("Telefone: ")

        return {'nome': nome, 'telefone': telefone}    