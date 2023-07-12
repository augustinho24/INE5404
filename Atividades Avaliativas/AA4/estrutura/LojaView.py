from LojaController import LojaController

class FuncionarioView:
    def __init__(self, controller):
        self.controller = controller

    def cadastrarFuncionario(self):
        print("\nCadastro de Funcionário\n")
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        id_funcionario = input("Digite o ID: ")
        telefone = input("Digite o telefone: ")
        salario = input("Digite o salário: ")
        cargo = input("Digite o cargo: ")
        self.controller.criar_funcionario(nome, cpf, id_funcionario, telefone, salario, cargo)
        print("\nFuncionário cadastrado com sucesso!\n")

    def listarFuncionario(self): 
        if len(self.controller.model.funcionarios) == 0:
            print("\nNão há funcionários cadastrados.\n")
        for c in self.controller.model.funcionarios:
            print("\n","/"*50)
            print(f"Nome: {c.nome}")
            print(f"CPF: {c.cpf}")
            print(f"ID: {c.id_funcionario}")
            print(f"Telefone: {c.telefone}")
            print(f"Salário: R$ {c.salario}")
            print(f"Cargo: {c.cargo}")
            print("/"*50,"\n")

    def atualizarFuncionario(self):
        print("\nAtualizar Funcionário\n")
        id_funcionario = input("Digite o ID do funcionário: ")
        funcionario = self.controller.obter_funcionario(id_funcionario)
        if funcionario:
            novo_nome = input("Digite o novo nome: ")
            novo_cpf = input("Digite o novo CPF: ")
            novo_telefone = input("Digite o novo telefone: ")
            novo_salario = input("Digite o novo salário: ")
            novo_cargo = input("Digite o novo cargo: ")
            self.controller.atualizar_funcionario(id_funcionario, novo_nome, novo_cpf, novo_telefone, novo_salario, novo_cargo)
            print("Funcionário atualizado com sucesso!\n")
        else:
            print("Funcionário não encontrado!\n")
        
    def deletarFuncionario(self):
        print("\nDeletar Funcionário\n")
        id_funcionario = input("Digite o ID do funcionário: ")
        funcionario = self.controller.obter_funcionario(id_funcionario)
        if funcionario:
            self.controller.deletar_funcionario(id_funcionario)
            print("Funcionário deletado com sucesso!\n")
        else:
            print("Funcionário não encontrado!\n")       

class ClienteView:
    def __init__(self, controller):
        self.controller = LojaController()
    
    def cadastrarCliente(self):
        print("\nCadastro de Cliente\n")
        cpf = input("Digite o CPF: ")
        nome = input("Digite o nome: ")
        id_cliente = input("Digite o ID: ")
        endereco = input("Digite o endereço: ")
        email = input("Digite o email: ")
        senha = input("Digite a senha: ")
        historico_compras = []
        self.controller.criar_cliente(cpf, nome, id_cliente, endereco, email, senha, historico_compras)
        print("Cliente cadastrado com sucesso!\n")
    
    def listarCliente(self):
        if len(self.controller.model.clientes) == 0:
            print("\nNão há clientes cadastrados.\n")
        for c in self.controller.model.clientes:
            print("\n","/"*50)
            print(f"CPF: {c.cpf}")
            print(f"Nome: {c.nome}")
            print(f"ID: {c.id_cliente}")
            print(f"Endereço: {c.endereco}")
            print(f"Email: {c.email}")
            print(f"Senha: {c.senha}")
            print(f"Histórico de Compras: {c.historico_compras}")
            print("/"*50, "\n")

    def atualizarCliente(self):
        print("\nAtualizar Cliente\n")
        id_cliente = input("Digite o ID do cliente: ")
        cliente = self.controller.obter_cliente(id_cliente)
        if cliente:
            novo_cpf = input("Digite o novo CPF: ")
            novo_nome = input("Digite o novo nome: ")
            novo_endereco = input("Digite o novo endereço: ")
            novo_email = input("Digite o novo email: ")
            nova_senha = input("Digite a nova senha: ")
            self.controller.atualizar_cliente(id_cliente, novo_cpf, novo_nome, novo_endereco, novo_email, nova_senha)
            print("Cliente atualizado com sucesso!\n")
        else:
            print("Cliente não encontrado!\n")
        
    def deletarCliente(self):
        print("\nDeletar Cliente\n")
        id_cliente = input("Digite o ID do cliente: ")
        cliente = self.controller.obter_cliente(id_cliente)
        if cliente:
            self.controller.deletar_cliente(id_cliente)
            print("Cliente deletado com sucesso!\n")
        else:
            print("Cliente não encontrado!\n")
        
class ProdutoView:
    def __init__(self, controller):
        self.controller = LojaController()

    def cadastrarProduto(self):
        print("\nCadastro de Produto\n")   
        departamento = input("Digite o departamento (Adulto ou Infantil): ").lower()
        while departamento.lower() not in ["adulto", "infantil"]:
            print("Departamento inválido. Por favor, digite 'Adulto' ou 'Infantil'.")
            departamento = input("Digite o departamento: ").lower()

        tipo = input("Digite o tipo: ")
        tamanho = input("Digite o tamanho (PP, P, M, G, GG, XG): ").upper()
        while tamanho.upper() not in ["PP", "P", "M", "G", "GG", "XG"]:
            print("Tamanho inválido. Por favor, digite um tamanho válido.")
            tamanho = input("Digite o tamanho: ").upper()

        genero = input("Digite o gênero (Feminino ou Masculino ou Unissex): ")
        while genero.lower() not in ["feminino", "masculino", "unissex"]:
            print("Gênero inválido. Por favor, digite 'Feminino' ou 'Masculino'.")
            genero = input("Digite o gênero: ").lower()

        unidades = int(input("Digite a quantidade de unidades: "))
        while unidades <= 0:
            print("Quantidade inválida. Por favor, digite um número positivo.")
            unidades = int(input("Digite a quantidade de unidades: "))

        codigo_serial = input("Digite o código serial: ")
        for i in self.controller.model.produtos:
            while i.codigo_serial == codigo_serial:
                print("Código serial já cadastrado. Por favor, digite um código serial válido.")
                codigo_serial = input("Digite o código serial: ")

        preco = float(input("Digite o preço: "))
        while preco <= 0:
            print("Preço inválido. Por favor, digite um número positivo.")
            preco = float(input("Digite o preço: "))
        self.controller.criar_produto(departamento, tipo, tamanho, genero, unidades, codigo_serial, preco)
        print("Produto cadastrado com sucesso!\n")

    def listarProduto(self): #amém
        if len(self.controller.model.produtos) == 0:
            print("\nNão há produtos cadastrados.\n")
        for p in self.controller.model.produtos:
            print("")
            print("\n","/"*50)
            print(f"Departamento: {p.departamento}") 
            print(f"Tipo: {p.tipo}")
            print(f"Tamanho: {p.tamanho}")
            print(f"Gênero: {p.genero}")
            print(f"Unidades: {p.unidades}")
            print(f"Código serial: {p.codigo_serial}")
            print(f"Preço: R$ {p.preco}")
            print("\n","/"*50)
    
    def atualizarProduto(self):
        print("\nAtualizar Produto\n")
        codigo_serial = input("Digite o código serial do produto: ")
        produto = self.controller.obter_produto(codigo_serial)
        if produto:
            novo_departamento = input("Digite o novo departamento (Adulto ou Infantil): ").lower()
            while novo_departamento.lower() not in ["adulto", "infantil"]:
                print("Departamento inválido. Por favor, digite 'Adulto' ou 'Infantil'.")
                novo_departamento = input("Digite o novo departamento: ").lower()
            
            novo_tipo = input("Digite o novo tipo: ")
            novo_tamanho = input("Digite o novo tamanho (PP, P, M, G, GG, XG): ").upper()
            while novo_tamanho.upper() not in ["PP", "P", "M", "G", "GG", "XG"]:
                print("Tamanho inválido. Por favor, digite um tamanho válido.")
                novo_tamanho = input("Digite o novo tamanho: ").upper()
            
            novo_genero = input("Digite o novo gênero (Feminino ou Masculino ou Unissex): ").lower()
            while novo_genero.lower() not in ["feminino", "masculino", "unissex"]:
                print("Gênero inválido. Por favor, digite 'Feminino' ou 'Masculino'.")
                novo_genero = input("Digite o novo gênero: ").lower()
            
            novo_unidades = int(input("Digite a nova quantidade de unidades: "))
            while novo_unidades <= 0:
                print("Quantidade inválida. Por favor, digite um número positivo.")
                novo_unidades = int(input("Digite a nova quantidade de unidades: "))
            
            novo_codigo_serial = input("Digite o novo código serial: ")
            for i in self.controller.model.produtos:
                while i.codigo_serial == novo_codigo_serial:
                    print("Código serial já cadastrado. Por favor, digite um código serial válido.")
                    novo_codigo_serial = input("Digite o novo código serial: ")
            
            novo_preco = float(input("Digite o novo preço: "))
            while novo_preco <= 0:
                print("Preço inválido. Por favor, digite um número positivo.")
                novo_preco = float(input("Digite o novo preço: "))
            
            self.controller.atualizar_produto(codigo_serial,novo_departamento, novo_tipo, novo_tamanho, novo_genero, novo_unidades, novo_codigo_serial, novo_preco)        
            print("Produto atualizado com sucesso!\n")
        else:
            print("Produto não encontrado!\n")

    def deletarProduto(self):
        print("\nDeletar Produto\n")
        codigo_serial = input("Digite o código serial do produto: ")
        produto = self.controller.obter_produto(codigo_serial)
        if produto:
            self.controller.deletar_produto(codigo_serial)
            print("Produto deletado com sucesso!\n")
        else:
            print("Produto não encontrado!\n")

class Menu:
    def __init__(self):
        self.controller = LojaController()
        self.funcionarioView = FuncionarioView(self.controller)
        self.clienteView = ClienteView(self.controller)
        self.produtoView = ProdutoView(self.controller)
        self.opcao = 0

    def exibirMenu(self):
        while self.opcao != 4:
            print("Menu Principal\n")
            print("1 - Funcionário")
            print("2 - Cliente")
            print("3 - Produto")
            print("4 - Sair\n")
            self.opcao = int(input("Digite a opção desejada: "))
            if self.opcao == 1:
                self.menuFuncionario()
            elif self.opcao == 2:
                self.menuCliente()
            elif self.opcao == 3:
                self.menuProduto()
            elif self.opcao == 4:
                print("Saindo...")
            else:
                print("Opção inválida. Por favor, digite uma opção válida.\n")
    
    def menuFuncionario(self):
        while self.opcao != 5:
            print("Menu Funcionário\n")
            print("1 - Cadastrar Funcionário")
            print("2 - Listar Funcionário")
            print("3 - Atualizar Funcionário")
            print("4 - Deletar Funcionário")
            print("5 - Voltar\n")
            self.opcao = int(input("Digite a opção desejada: "))
            if self.opcao == 1:
                self.funcionarioView.cadastrarFuncionario()
            elif self.opcao == 2:
                self.funcionarioView.listarFuncionario()
            elif self.opcao == 3:
                self.funcionarioView.atualizarFuncionario()
            elif self.opcao == 4:
                self.funcionarioView.deletarFuncionario()
            elif self.opcao == 5:
                print("Voltando...")
            else:
                print("Opção inválida. Por favor, digite uma opção válida.\n")
            
    def menuCliente(self):
        while self.opcao != 5:
            print("Menu Cliente\n")
            print("1 - Cadastrar Cliente")
            print("2 - Listar Cliente")
            print("3 - Atualizar Cliente")
            print("4 - Deletar Cliente")
            print("5 - Voltar\n")
            self.opcao = int(input("Digite a opção desejada: "))
            if self.opcao == 1:
                self.clienteView.cadastrarCliente()
            elif self.opcao == 2:
                self.clienteView.listarCliente()
            elif self.opcao == 3:
                self.clienteView.atualizarCliente()
            elif self.opcao == 4:
                self.clienteView.deletarCliente()
            elif self.opcao == 5:
                print("Voltando...")
            else:
                print("Opção inválida. Por favor, digite uma opção válida.\n")
        
    def menuProduto(self):
        while self.opcao != 5:
            print("Menu Produto\n")
            print("1 - Cadastrar Produto")
            print("2 - Listar Produto")
            print("3 - Atualizar Produto")
            print("4 - Deletar Produto")
            print("5 - Voltar\n")
            self.opcao = int(input("Digite a opção desejada: "))
            if self.opcao == 1:
                self.produtoView.cadastrarProduto()
            elif self.opcao == 2:
                self.produtoView.listarProduto()
            elif self.opcao == 3:
                self.produtoView.atualizarProduto()
            elif self.opcao == 4:
                self.produtoView.deletarProduto()
            elif self.opcao == 5:
                print("Voltando...")
            else:
                print("Opção inválida. Por favor, digite uma opção válida.\n")



        
    

        



