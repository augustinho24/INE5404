'''Você deve implementar um sistema de Locação de Automóveis, a locadora deverá ter armazenar (em listas) 
as informações de clientes, veículos e funcionários, assim como reservas e locações dos automóveis.'''
"""- Utilização de Herança, composição e agregação ; 
- Criação, Edição, consulta , remoção das informações  e login; """

# Importando as classes
from pessoa import Pessoa, Cliente, Funcionario

class Main():
    def __init__(self):
        pass
    lista_Clientes = []
    lista_Funcionarios = []
    lista_Veiculos_disponiveis = []
    lista_Veiculos_locados = []
    ids_cadastrados = set() # Para não haver repetição de senhas de pessoas
    senhas_cadastrados = set() # Para não haver repetição de ids de pessoas
    ids_veiculos_cadastrados = set() # Para não haver repetição de ids de veiculos

    def cadastro(self):
        print("\n1 - Cliente\n2 - Funcionario\n")
        tipo_cadastro = int(input("Digite o tipo de cadastro: "))
        while tipo_cadastro < 1 or tipo_cadastro > 2:
            print("Opção invalida")
            print("\n\n1 - Cliente\n2 - Funcionario\n")
            tipo_cadastro = int(input("Digite o tipo de cadastro: "))      
        if tipo_cadastro == 1:
            self.cadastro_Cliente()
        elif tipo_cadastro == 2:
            self.cadastro_Funcionario()
        else:
            print("Opção inválida")
            self.cadastro()
        
    def cadastro_Cliente(self):
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")
        idade = input("Digite sua idade: ")
        id = input("Digite um id: ")
        while id in self.ids_cadastrados:
            print("ID já cadastrado")
            id = input("Digite um ID: ")
        senha = input("Digite uma senha: ")
        while senha in self.senhas_cadastrados:
            print("Senha já cadastrado")
            senha = input("Digite uma senha: ")    
        historico_locacao = []
        veiculos_alugados = []
        cliente = Cliente(nome, cpf, idade, id, senha, historico_locacao, veiculos_alugados)
        self.lista_Clientes.append(cliente)
        self.ids_cadastrados.add(id)
        self.senhas_cadastrados.add(senha)  
        print("Cadastro realizado com sucesso")
        self.menu()
    
    def cadastro_Funcionario(self):
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")
        idade = input("Digite sua idade: ")
        id = input("Digite seu id: ")
        while id in self.ids_cadastrados:
            print("ID já cadastrado")
            id = input("Digite um ID: ")
        senha = input("Digite sua senha: ")
        while senha in self.senhas_cadastrados:
            print("Senha já cadastrada")
            senha = input("Digite sua senha: ")
        salario = float(input("Digite seu salario: "))
        print("\n\n1 - Administrador\n2 - Operador\n")
        opcao = int(input("Digite o cargo: "))
        if opcao == 1:
            cargo = "Administrador"
        elif opcao == 2:
            cargo = "Operador"
        funcionario = Funcionario(nome, cpf, idade, id, senha, salario, cargo)
        self.lista_Funcionarios.append(funcionario)
        self.ids_cadastrados.add(id)
        self.senhas_cadastrados.add(senha)
        print("Cadastro realizado com sucesso")
        self.menu()
    
    def exibir_Clientes(self):
        print("=" * 50)
        for cliente in self.lista_Clientes:
            print("Clientes cadastrados: \n")
            print("=" * 30)
            print("Nome: " ,cliente.get_nome())
            print("CPF:" ,cliente.get_cpf())
            print("Idade: " ,cliente.get_idade())
            print("ID:" ,cliente.get_id_pessoa())
            print("Historico de locação: " ,cliente.get_historico_locacao())
            print("Veiculos alugados: " ,cliente.get_veiculos_alugados())
            print("=" * 30)
        print("=" * 50)
        self.menu()

    def exibir_Funcionarios(self):
        print("=" * 50)
        for funcionario in self.lista_Funcionarios:
            print("Funcionários cadastrados: \n")
            print("=" * 30)
            print("Nome: " ,funcionario.get_nome())
            print("CPF:" ,funcionario.get_cpf())
            print("Idade: " ,funcionario.get_idade())
            print("ID:" ,funcionario.get_id_pessoa())
            print("Salario: " ,funcionario.get_salario())
            print("Cargo: " ,funcionario.get_cargo())
            print("=" * 30)
        print("=" * 50)
        self.menu()

    def alterar_Cliente(self):
        id = input("Digite o id do cliente que deseja alterar: ")
        for cliente in self.lista_Clientes:
            if cliente.get_id_pessoa() == id:
                self.cliente = cliente
            else:
                print("Cliente não encontrado")
                self.menu()
        print("O que deseja alterar? \n")
        print("1 - Nome\n2 - CPF\n3 - Idade\n4 - ID\n5 - Senha\n")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            nome = input("Digite o novo nome: ")
            self.cliente.set_nome(nome)
        elif opcao == 2:
            cpf = input("Digite o novo cpf: ")
            self.cliente.set_cpf(cpf)
        elif opcao == 3:
            idade = input("Digite a nova idade: ")
            self.cliente.set_idade(idade)
        elif opcao == 4:
            id = input("Digite o novo id: ")
            while id in self.ids_cadastrados and id != self.cliente.get_id_pessoa():
                print("ID já cadastrado")
                id = input("Digite um ID: ")
            #remover o id antigo da lista de ids
            self.ids_cadastrados.remove(self.cliente.get_id_pessoa())
            self.cliente.set_id_pessoa(id)
        elif opcao == 5:
            senha = input("Digite a nova senha: ")
            while senha in self.senhas_cadastrados and senha != self.cliente.get_senha():
                print("Senha já cadastrada")
                senha = input("Digite sua senha: ")
            #remover a senha antiga da lista de senhas
            self.senhas_cadastrados.remove(self.cliente.get_senha())
            self.cliente.set_senha(senha)
        else:
            print("Opção inválida")
            self.alterar_Cliente()
        print("Alteração realizada com sucesso")
        self.menu()

    def alterar_Funcionario(self):
        id = input("Digite o id do funcionario que deseja alterar: ")
        for funcionario in self.lista_Funcionarios: 
            if funcionario.get_id_pessoa() == id:
                self.funcionario = funcionario
            else:
                print("Funcionario não encontrado")
                self.menu()
        print("O que deseja alterar? \n")
        print("1 - Nome\n2 - CPF\n3 - Idade\n4 - ID\n5 - Senha\n6 - Salario\n7 - Cargo\n")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            nome = input("Digite o novo nome: ")
            self.funcionario.set_nome(nome)
        elif opcao == 2:
            cpf = input("Digite o novo cpf: ")
            self.funcionario.set_cpf(cpf)
        elif opcao == 3:
            idade = input("Digite a nova idade: ")
            self.funcionario.set_idade(idade)
        elif opcao == 4:
            id = input("Digite o novo id: ")
            while id in self.ids_cadastrados and id != self.funcionario.get_id_pessoa():
                print("ID já cadastrado")
                id = input("Digite um ID: ")
            #remover o id antigo da lista de ids
            self.ids_cadastrados.remove(self.funcionario.get_id_pessoa())
            self.funcionario.set_id_pessoa(id)
        elif opcao == 5:
            senha = input("Digite a nova senha: ")
            self.funcionario.set_senha(senha)
            while senha in self.senhas_cadastrados and senha != self.funcionario.get_senha():
                print("Senha já cadastrado")
                senha = input("Digite sua senha: ")
            #remover a senha antiga da lista de senhas
            self.senhas_cadastrados.remove(self.funcionario.get_senha())
            self.funcionario.set_senha(senha)
        elif opcao == 6:
            salario = input("Digite o novo salario: ")
            self.funcionario.set_salario(salario)
        elif opcao == 7:
            print("\n\n1 - Administrador\n2 - Operador\n")
            opcao = int(input("Digite o cargo: "))
            if opcao == 1:
                cargo = "Administrador"
            elif opcao == 2:
                cargo = "Operador"
            self.funcionario.set_cargo(cargo)
        else:
            print("Opção inválida")
            self.alterar_Funcionario()
        print("Alteração realizada com sucesso")
        self.menu()
    
    def excluir_Cliente(self):
        id = input("Digite o id do cliente que deseja excluir: ")
        for cliente in self.lista_Clientes:
            if cliente.get_id_pessoa() == id:
                self.cliente = cliente
            else:
                print("Cliente não encontrado")
                self.menu()
        self.lista_Clientes.remove(self.cliente)
        #remover o id antigo da lista de ids
        self.ids_cadastrados.remove(self.cliente.get_id_pessoa())
        #remover a senha antiga da lista de senhas
        self.senhas_cadastrados.remove(self.cliente.get_senha())
        print("Cliente excluido com sucesso")
        self.menu()
    
    def excluir_Funcionario(self):
        id = input("Digite o id do funcionario que deseja excluir: ")
        for funcionario in self.lista_Funcionarios:
            if funcionario.get_id_pessoa() == id:
                self.funcionario = funcionario
            else:
                print("Funcionario não encontrado")
                self.menu()
        self.lista_Funcionarios.remove(self.funcionario)
        #remover o id antigo da lista de ids
        self.ids_cadastrados.remove(self.funcionario.get_id_pessoa())
        #remover a senha antiga da lista de senhas
        self.senhas_cadastrados.remove(self.funcionario.get_senha())
        print("Funcionario excluido com sucesso")
        self.menu()
    
    #testando menu sem restrição de login
    def menu(self):
        print("Fogaréu Rent de 30 de Fevereiro\n")
        print("1 - Login")
        print("2 - Cadastro")
        print("3 - Listar Clientes")
        print("4 - Listar Funcionarios")
        print("5 - Excluir Cliente")
        print("6 - Excluir Funcionario")
        print("7 - Alterar Cliente")
        print("8 - Alterar Funcionario")

        print("0 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 0:
            print("Obrigado por utilizar o sistema de locação de automóveis")
            exit()
        elif opcao == 1:
            self.login()
        elif opcao == 2:
            self.cadastro()
        elif opcao == 3:
            self.exibir_Clientes()
        elif opcao == 4:
            self.exibir_Funcionarios()
        elif opcao == 5:
            self.excluir_Cliente()
        elif opcao == 6:
            self.excluir_Funcionario()
        elif opcao == 7:
            self.alterar_Cliente()
        elif opcao == 8:
            self.alterar_Funcionario()
        else:
            print("Opção inválida")
            self.menu()
    


while True:
    main = Main()
    main.menu()



    





