from Produtos import *

class Informacoes:
    def __init__(self):
        self.listaProdutos = []

    def salvar_produtos(self):
        entrada_cod = input('Informe o código: ')
        entrada_descricao = input('Informe a Descricao: ')
        entrada_fabricante = input('Informe o Fabricante: ')
        entrada_quantidade = input('Informe a Quantidade: ')
        self.listaProdutos.append(Produtos(cod=entrada_cod,
                                          descricao=entrada_descricao,
                                          fabricante=entrada_fabricante,
                                          quantidade=entrada_quantidade))
        print('Produto Salvo!')

    def listar_todos_produtos(self):
        for i in range(len(self.listaProdutos)):
            print('Cod:', self.listaProdutos[i].cod,
                  '- Descricao:', self.listaProdutos[i].descricao,
                  '- Fabricante:', self.listaProdutos[i].fabricante,
                  '- Quantidade:', self.listaProdutos[i].quantidade)

    def procurar_produto(self):
        entrada = input('Informe o codigo do Produto: ')
        for i in range(len(self.listaProdutos)):
            if entrada == self.listaProdutos[i].cod:
                print('Cod:', self.listaProdutos[i].cod,
                      '- Descricao:', self.listaProdutos[i].descricao,
                      '- Fabricante:', self.listaProdutos[i].fabricante,
                      '- Quantidade:', self.listaProdutos[i].quantidade)

    def alterar_produto(self):
        entrada = input('Informe o codigo do Produto: ')
        for i in range(len(self.listaProdutos)):
            if entrada == self.listaProdutos[i].cod:
                self.listaProdutos[i].descricao = input('Nova Descricao: ')
            else:
                cont = 0
                cont += 1
                if cont == len(self.listaProdutos):
                    print('Codigo Nao Cadastrado')