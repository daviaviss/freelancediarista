from telas.tela_abstrata import *

class TelaSistema:
    def tela_inicial(self):
        cabecalho('BEM-VINDO(A)')
        opcoes = ['[1] Fazer Login','[2] Criar uma conta', '[0] Encerrar Programa']

        for item in opcoes:
            print(item)

        print(linha())
        opcao = ler_int('Digite sua opção: ')
        return opcao