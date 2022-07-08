from Informacoes import *

class Menu:
    def __init__(self):
        informacoes = Informacoes()

        # Iniciar
        while True:
            entrada = input('Informe o que Deseja\n1'
                            ' - Novo Produto\n2'
                            ' - Listar Produtos\n3'
                            ' - Alterar Produto\n4'
                            ' - Procurar Produtos\n5'
                            ' - Comprar\n6'
                            ' - Vender\n0'
                            ' - Sair')

            if entrada == '1':
                informacoes.salvar_produtos()
            elif entrada == '2':
                informacoes.listar_todos_produtos()
            elif entrada == '3':
                informacoes.alterar_produto()
            elif entrada == '4':
                informacoes.procurar_produto()
            elif entrada == '0':
                break
            else:
                print('Opção Incorreta!')