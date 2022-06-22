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
    
    def tela_login(self):
        cabecalho('ESCOLHA UMA OPÇÃO')
        opcoes = ['[1] Login Contratante','[2] Login Diarista']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = ler_int('Digite sua opção: ')
        return opcao

    def tela_opcoes_contratante(self):
        
        cabecalho('ESCOLHA UMA OPÇÃO')
        opcoes = ['[1] Listar Trabalhos','[2] Cadastrar Trabalho','[3] Editar Trabalho', '[4] Excluir Trabalho', '[0] Finalizar Sessão']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = ler_int('Digite sua opção: ')
        return opcao


    def tela_opcoes_diarista(self):
        
        cabecalho('ESCOLHA UMA OPÇÃO')
        opcoes = ['[1] Listar Trabalhos','[2] Aceitar Trabalho','[3] Deixar Trabalho', '[4] Meus Trabalhos', '[0] Finalizar Sessão']
        
        for item in opcoes:
            print(item)

        print(linha())

        opcao = ler_int('Digite sua opção: ')
        return opcao