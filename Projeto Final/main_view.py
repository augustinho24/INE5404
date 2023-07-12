from data_pessoas import BD_Pessoas
from data_produtos import BD_Produtos
from controll_pessoas import Controller_BD_pessoas
from controll_produtos import Controller_BD_produtos
from model_produto import *
from model_compra import *
from model_pessoa import *
from random import randint
from datetime import *

class MainInterface:
    def __init__(self):
        self.bd_pessoas = BD_Pessoas()
        self.bd_produtos = BD_Produtos()
        self.controller_pessoas = Controller_BD_pessoas()
        self.controller_produtos = Controller_BD_produtos()

    def adicionar_produto_ao_carrinho(self, cliente): # Adiciona produto ao carrinho
        produto =  self.controller_produtos.buscar_produto()
        if produto == None:
            print("Produto não encontrado!")
            return
        try:
            quantidade = int(input("Digite a quantidade do produto que deseja adicionar ao carrinho: "))
        except ValueError:
            print("Quantidade inválida!")
            return
        if quantidade <= 0:
            print("Quantidade inválida!")
            return

        cliente.add_produto_carrinho(produto, quantidade)
        print("Produto adicionado ao carrinho com sucesso!")


    def remover_produto_do_carrinho(self, cliente): # Remove produto do carrinho
        try:
            produto = self.controller_produtos.buscar_produto()
        except ValueError:
            print("Id inválido!")
            return
        if produto == None:
            print("Produto não encontrado!")
            return
        elif cliente.remover_produto_carrinho(produto) == False:
            print("Produto não encontrado no carrinho!")
            return
        else:
            print("Produto removido do carrinho com sucesso!")
            return


    def listar_produtos_do_carrinho(self, cliente): # Exibe produtos do carrinho, através do método listar_carrinho() da classe Cliente
        cliente.listar_carrinho()
        print('#' * 60, '\n')
    
    def listar_produtos_historico_cliente(self, cliente): # Exibe produtos do histórico de compras do cliente, através do método listar_historico_compras() da classe Cliente
        cliente.listar_historico_compras()
        print('#' * 60, '\n')
            
        
    
    def finalizar_compra(self, cliente): # Finaliza a compra
        # Verifica se o carrinho está vazio
        if len(cliente.carrinho) == 0:
            print("Carrinho vazio!")
            return
        # verifica se há quantidade suficiente de cada produto no estoque
        for produto, quantidade in cliente.carrinho.items():
            if produto.quantidade < quantidade:
                print(f"Quantidade insuficiente do produto {produto.nome}!")
                return
        # gera um id de compra aleatório
        id_compra = randint(100000000000000, 999999999999999)
        while self.bd_pessoas.verifica_id_compra(id_compra):
            id_compra = randint(100000000000000, 999999999999999)
        # gera a data da compra
        data_compra = datetime.now()

        cliente.listar_carrinho()
        print('#' * 60, '\n')

        valor_total = 0
        for produto, quantidade in cliente.carrinho.items(): # somar o valor total da compra
            valor_total += produto.preco * quantidade
        print(f"Valor total da compra: R$ {valor_total:.2f}")
        print('#' * 60, '\n')
        forma_pagamento = input("1 - Boleto bancário | 2 - Cartão de crédito\n Digite a opção de escolha para a forma de pagamento: ")
        while forma_pagamento not in ['1', '2']:
            print("Opção inválida!")
            forma_pagamento = input("1 - Boleto bancário | 2 - Cartão de crédito\n Digite a opção de escolha para a forma de pagamento: ")
        if forma_pagamento == '1':
            forma_pagamento = "Boleto bancário"
        else:
            forma_pagamento = "Cartão de crédito"
        print('#' * 60, '\n')
        # verifica se o cliente deseja finalizar a compra
        opcao = input("Deseja finalizar a compra? (S/N) ").upper()
        while opcao not in ['S', 'N']:
            print("Opção inválida!")
            opcao = input("Deseja finalizar a compra? (S/N) ").upper()
        if opcao == 'S':
            # atualiza a quantidade de cada produto no estoque
            for produto, quantidade in cliente.carrinho.items():
                produto.quantidade -= quantidade
                if produto.quantidade == 0:
                    self.bd_produtos.remover_produto(produto.id_produto) # remove o produto do banco de dados se a quantidade for igual a 0
            produtos = cliente.carrinho # dicionário contendo produto e suas respectivas quantidades
            # adiciona a compra ao histórico de compras do cliente
            compra = Compra(id_compra, data_compra, valor_total, forma_pagamento, produtos)
            cliente.add_compra_historico(compra)
            # adiciona o id da compra ao conjunto de ids de compras
            self.bd_pessoas.conjunto_id_compras.add(id_compra)
            self.bd_pessoas.add_compra_lista(compra)
            # esvazia o carrinho
            cliente.carrinho.clear()
            print("Compra finalizada com sucesso!")
            return



    def login_cliente(self): #### verificar se o usuário e a senha estão corretos (associados a um cliente)
        print("#" * 20, "Login do cliente", "#" * 20)
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")
        clientes = self.controller_pessoas.pega_lista_clientes()
        for cliente in clientes:
            if cliente.usuario == usuario and cliente.senha == senha:
                 c = cliente
                 self.menu_cliente(c)
          
        print("Usuário ou senha incorretos!")
        return
    

    def menu_cliente(self,cliente): # Menu do cliente
        print("#" * 20, "Menu do cliente", "#" * 20)
        print(f"\nBem-vindo, {cliente.nome}!" "\n")
        print("#" * 60, "\n")

        print("=" * 20, "Produtos", "=" * 20)
        print("1 - Listar produtos")
        print("2 - Adicionar produto ao carrinho")
        print("3 - Remover produto do carrinho")
        print("4 - Listar produtos do carrinho")
        print("5 - Finalizar compra")
        print("6 - Listar histórico de compras\n")
        print("0 - Sair")
        print("#" * 60, "\n")
        opcao = input("Digite a opção desejada: ")
        while opcao not in ['1', '2', '3', '4', '5', '6', '0']:
            print("Opção inválida!")
            opcao = input("Digite a opção desejada: ")
        if opcao == '1':
            self.controller_produtos.listar_produtos()
            self.menu_cliente(cliente) # retorna para o menu do cliente
        elif opcao == '2':
            self.adicionar_produto_ao_carrinho(cliente)
            self.menu_cliente(cliente) 
        elif opcao == '3':
            self.remover_produto_do_carrinho(cliente)
            self.menu_cliente(cliente) 
        elif opcao == '4':
            self.listar_produtos_do_carrinho(cliente)
            self.menu_cliente(cliente)
        elif opcao == '5':
            self.finalizar_compra(cliente)
            self.menu_cliente(cliente)
        elif opcao == '6':
            self.listar_produtos_historico_cliente(cliente)
            self.menu_cliente(cliente)
        elif opcao == '0':
            self.main()

    def login_adm(self): # Verifica se o usuário e a senha estão corretos (pré-definidos)
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")
        if usuario == "mangastore" and senha == "adm123":
            return True
        else:
            return False

    def menu_adm(self): # Menu do administrador
        print("#" * 20, "Menu do administrador", "#" * 20)
        print("\nBem-vindo, mangastore (Admim)!".center(60), "\n")
        print("#" * 60, "\n")
        print("=" * 20, "Produtos", "=" * 20)
        print("1 - Cadastrar produto")
        print("2 - Alterar produto")
        print("3 - Excluir produto")
        print("4 - Listar produtos\n")
        print("=" * 20, "Clientes", "=" * 20)
        print("6 - Cadastrar cliente")
        print("7 - Alterar cliente")
        print("8 - Excluir cliente")
        print("9 - Listar clientes")
        print("0 - Sair")
        print("#" * 60, "\n")
        opcao = input("Digite a opção desejada: ")
        while opcao not in ['1', '2', '3', '4', '6', '7', '8', '9', '0']:
            print("Opção inválida!")
            opcao = input("Digite a opção desejada: ")
        if opcao == '1':
            self.controller_produtos.cadastrar_produto()
            self.menu_adm()
        elif opcao == '2':
            self.controller_produtos.alterar_produto()
            self.menu_adm()
        elif opcao == '3':
            self.controller_produtos.remover_produto()
            self.menu_adm()
        elif opcao == '4':
            self.controller_produtos.listar_produtos()
            self.menu_adm()
        elif opcao == '6':
            self.controller_pessoas.cadastrar_cliente()
            self.menu_adm()
        elif opcao == '7':
            self.controller_pessoas.alterar_cliente()
            self.menu_adm()
        elif opcao == '8':
            self.controller_pessoas.remover_cliente()
            self.menu_adm()
        elif opcao == '9':
            self.controller_pessoas.listar_clientes()
            self.menu_adm()
        elif opcao == '0':
            self.main()

    def main(self): # Menu principal/inicial
        print("#" * 20, "Menu principal", "#"* 20)
        print("1 - Login Administrador")
        print("2 - Login Cliente")
        print("3 - Cadastrar Cliente")
        #print("4 - TESTE - VERIFICAR LISTA DE CLIENTES")
        #print("5 - VERIFICA PRODUTO POR ID")
        print("0 - Sair")
        print("#" * 60, "\n")
        opcao = input("Digite a opção desejada: ")
        while opcao not in ['1', '2', '3', '4', '5', '0']:
            print("Opção inválida!")
            opcao = input("Digite a opção desejada: ")
        if opcao == '1':
            if self.login_adm():
                self.menu_adm()
            else:
                print("Usuário ou senha incorretos!")
                self.main()
        elif opcao == '2':
            self.login_cliente()
            self.main()
        elif opcao == '3':
            self.controller_pessoas.cadastrar_cliente()
            self.main()
        elif opcao == '4': # TESTE
            lista = self.controller_pessoas.pega_lista_clientes()
            lista2 = self.controller_produtos.pega_lista_produtos()
            print(lista)
            print("QTD CLIENTES: ", len(lista))
            print(lista2)
            print("QTD PRODUTOS: ", len(lista2))
            self.main()
        elif opcao == '5': # TESTE
            self.controller_produtos.buscar_produto()
            if self.controller_produtos.buscar_produto:
                print("Produto encontrado!")
            else:
                print("Produto não encontrado!")
            self.main()
        elif opcao == '0':
            exit()

