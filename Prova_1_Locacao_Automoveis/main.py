# Importando as classes
from pessoa import Pessoa, Cliente, Funcionario
from veiculo import Veiculo
from locacao import Locacao

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
    mster_password = "agostinho carrara" # Chave para permitir o cadastro de funcionarios, cujo cargo seja "Administrador". 

    def cadastrar_Veiculo(self):
        id_veiculo = input("Digite o id do veiculo: ")
        while id_veiculo in self.ids_veiculos_cadastrados or id_veiculo == '0':
            print("ID já cadastrado")
            id_veiculo = input("Digite o id do veiculo: ")
        placa = input("Digite a placa do veiculo: ")
        marca = input("Digite a marca do veiculo: ")
        modelo = input("Digite o modelo do veiculo: ")
        ano = input("Digite o ano do veiculo: ")
        valor_diaria = float(input("Digite o valor da diaria do veiculo: "))
        qtd_portas = input("Digite a quantidade de portas do veiculo: ")
        qtd_passageiros = input("Digite a quantidade de passageiros do veiculo: ")
        cambio = input("Digite o tipo de cambio do veiculo: ")
        disponivel = "Sim"
        veiculo = Veiculo(id_veiculo, placa, marca, modelo, ano, valor_diaria, qtd_portas, qtd_passageiros, cambio, disponivel)
        self.lista_Veiculos_disponiveis.append(veiculo)
        self.ids_veiculos_cadastrados.add(id_veiculo)
        print("Cadastro realizado com sucesso")
        self.menu_Funcionario()
    
    def alterar_Veiculo(self):
        while True:
            id_veiculo = input("Digite o id do veiculo (0 para sair): ")
            if id_veiculo == '0':
                self.menu_Funcionario()
            while id_veiculo not in self.ids_veiculos_cadastrados:
                print("ID não cadastrado")
                id_veiculo = input("Digite o id do veiculo: ")
                if id_veiculo == '0':
                    self.menu_Funcionario()
            for veiculo in self.lista_Veiculos_disponiveis:
                if veiculo.get_id_veiculo() == id_veiculo:
                    print("O que deseja alterar?")
                    print("1 - Placa\n2 - Marca\n3 - Modelo\n4 - Ano\n5 - Valor da diaria\n6 - Quantidade de portas\n7 - Quantidade de passageiros\n8 - Tipo de cambio\n9 - Sair")
                    while True:
                        opcao = int(input("Digite a opção: "))
                        if opcao == 1:
                            placa = input("Digite a placa do veiculo: ")
                            veiculo.set_placa(placa)
                        elif opcao == 2:
                            marca = input("Digite a marca do veiculo: ")
                            veiculo.set_marca(marca)
                        elif opcao == 3:
                            modelo = input("Digite o modelo do veiculo: ")
                            veiculo.set_modelo(modelo)
                        elif opcao == 4:
                            ano = input("Digite o ano do veiculo: ")
                            veiculo.set_ano(ano)
                        elif opcao == 5:
                            valor_diaria = float(input("Digite o valor da diaria do veiculo: "))
                            veiculo.set_valor_diaria(valor_diaria)
                        elif opcao == 6:
                            qtd_portas = input("Digite a quantidade de portas do veiculo: ")
                            veiculo.set_qtd_portas(qtd_portas)
                        elif opcao == 7:
                            qtd_passageiros = input("Digite a quantidade de passageiros do veiculo: ")
                            veiculo.set_qtd_passageiros(qtd_passageiros)
                        elif opcao == 8:
                            cambio = input("Digite o tipo de cambio do veiculo: ")
                            veiculo.set_cambio(cambio)
                        elif opcao == 9:
                            break
                        else:
                            print("Opção inválida")
                    print("Alteração realizada com sucesso")
                    self.menu_Funcionario()
  
   
    def exibir_Veiculos(self):
        print("=" * 50)
        for veiculo in self.lista_Veiculos_disponiveis:
            print("=" * 30)
            print("ID: ", veiculo.get_id_veiculo())
            print("Placa: ", veiculo.get_placa())
            print("Marca: ", veiculo.get_marca())
            print("Modelo: ", veiculo.get_modelo())
            print("Ano: ", veiculo.get_ano())
            print("Valor da diaria: R$", veiculo.get_valor_diaria())
            print("Quantidade de portas: ", veiculo.get_qtd_portas())
            print("Quantidade de passageiros: ", veiculo.get_qtd_passageiros())
            print("Tipo de cambio: ", veiculo.get_cambio())
            print("Disponivel: ", veiculo.get_disponivel())
            print("=" * 30)
            print("\n")

    def excluir_Veiculo(self):
        id_veiculo = input("Digite o id do veiculo (0 para sair): ")
        if id_veiculo == "0":
            self.menu_Funcionario()
        while id_veiculo not in self.ids_veiculos_cadastrados:
            print("ID não cadastrado")
            id_veiculo = input("Digite o id do veiculo: ")
            if id_veiculo == "0":
                self.menu_Funcionario()
        for veiculo in self.lista_Veiculos_disponiveis:
            if veiculo.get_id_veiculo() == id_veiculo:
                self.lista_Veiculos_disponiveis.remove(veiculo)
                self.ids_veiculos_cadastrados.remove(id_veiculo)
                print("Remoção realizada com sucesso")
                self.menu_Funcionario()
                 # Volta para o menu principal    

    def cadastrar_Pessoa(self):
        print("\n1 - Cliente\n2 - Funcionario\n")
        tipo_cadastro = int(input("Digite o tipo de cadastro: "))
        while tipo_cadastro < 1 or tipo_cadastro > 2:
            print("Opção invalida")
            print("\n\n1 - Cliente\n2 - Funcionario\n")
            tipo_cadastro = int(input("Digite o tipo de cadastro: "))      
        if tipo_cadastro == 1:
            self.cadastrar_Cliente()
        elif tipo_cadastro == 2:
            self.cadastrar_Funcionario()
        else:
            print("Opção inválida")
            self.cadastrar_Pessoa()
        
    def cadastrar_Cliente(self):
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
        
         # Volta para o menu principal

    
    def cadastrar_Funcionario(self):
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")
        idade = input("Digite sua idade: ")
        id = input("Digite um id: ")
        while id in self.ids_cadastrados:
            print("ID já cadastrado")
            id = input("Digite um ID: ")
        senha = input("Digite uma senha: ")
        while senha in self.senhas_cadastrados:
            print("Senha já cadastrada")
            senha = input("Digite uma senha: ")
        salario = float(input("Digite o salario: "))
        print("\n\n1 - Administrador\n2 - Operador\n")
        opcao = int(input("Digite o cargo: "))
        if opcao == 1:
            chave = input("Digite a chave de acesso: ")
            while chave != self.mster_password:
                print("Chave incorreta")
                chave = input("Digite a chave de acesso: ")
            cargo = "Administrador"
        elif opcao == 2:
            cargo = "Operador"
        funcionario = Funcionario(nome, cpf, idade, id, senha, salario, cargo)
        self.lista_Funcionarios.append(funcionario)
        self.ids_cadastrados.add(id)
        self.senhas_cadastrados.add(senha)
        print("Cadastro realizado com sucesso")

         # Volta para o menu principal

  
    def exibir_Clientes(self):
        print("=" * 50)
        for cliente in self.lista_Clientes:
            print("Clientes cadastrados: \n")
            print("=" * 30)
            print("Nome: " ,cliente.get_nome())
            print("CPF:" ,cliente.get_cpf())
            print("Idade: " ,cliente.get_idade())
            print("ID:" ,cliente.get_id_pessoa())
            print("=" * 30)
        print("=" * 50)

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

    def alterar_Cliente(self):
        id = input("Digite o id do cliente que deseja alterar: ")
        for cliente in self.lista_Clientes:
            if cliente.get_id_pessoa() == id:
                self.cliente = cliente
            else:
                print("Cliente não encontrado")
                self.menu_Funcionario()
        continuar_alterando = True
        while continuar_alterando:
            print("O que deseja alterar? \n")
            print("1 - Nome\n2 - CPF\n3 - Idade\n4 - ID\n5 - Senha\n6 - Finalizar alteração\n")
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
            elif opcao == 6:
                continuar_alterando = False
            else:
                print("Opção inválida")
        print("Alteração realizada com sucesso")
        self.menu_Funcionario()

    def alterar_Funcionario(self):
        id = input("Digite o id do funcionario que deseja alterar: ")
        for funcionario in self.lista_Funcionarios: 
            if funcionario.get_id_pessoa() == id:
                self.funcionario = funcionario
                break
        else:
            print("Funcionario não encontrado")
            self.menu_Funcionario()

        while True:
            print("O que deseja alterar? \n")
            print("1 - Nome\n2 - CPF\n3 - Idade\n4 - ID\n5 - Senha\n6 - Salario\n7 - Cargo\n8 - Sair")
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
                    print("Senha já cadastrada")
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
                    chave = input("Digite a chave de acesso: ")
                    while chave != self.mster_password:
                        print("Chave incorreta")
                        chave = input("Digite a chave de acesso: ")
                    cargo = "Administrador"
                elif opcao == 2:
                    cargo = "Operador"
                self.funcionario.set_cargo(cargo)
            elif opcao == 8:
                break
            else:
                print("Opção inválida")

        print("Alterações realizadas com sucesso")
        self.menu_Funcionario()
    
    def excluir_Cliente(self):
        id = input("Digite o id do cliente que deseja excluir: ")
        for cliente in self.lista_Clientes:
            if cliente.get_id_pessoa() == id:
                self.cliente = cliente
            else:
                print("Cliente não encontrado")
                self.menu_Funcionario()
        self.lista_Clientes.remove(self.cliente)
        #remover o id antigo da lista de ids
        self.ids_cadastrados.remove(self.cliente.get_id_pessoa())
        #remover a senha antiga da lista de senhas
        self.senhas_cadastrados.remove(self.cliente.get_senha())
        print("Cliente excluido com sucesso")
        self.menu_Funcionario()
    
    def excluir_Funcionario(self):
        id = input("Digite o id do funcionario que deseja excluir: ")
        for funcionario in self.lista_Funcionarios:
            if funcionario.get_id_pessoa() == id:
                self.funcionario = funcionario
            else:
                print("Funcionario não encontrado")
                self.menu_Funcionario()
        self.lista_Funcionarios.remove(self.funcionario)
        #remover o id antigo da lista de ids
        self.ids_cadastrados.remove(self.funcionario.get_id_pessoa())
        #remover a senha antiga da lista de senhas
        self.senhas_cadastrados.remove(self.funcionario.get_senha())
        print("Funcionário excluido com sucesso")
        self.menu_Funcionario()

    #Limitar o escopo de acesso do funcionario, ou seja, funções limitadas se e somente se o cargo do funcionário = "Administrador"
    def menu_Funcionario(self):
        print("="*60)
        print("Menu Funcionário".center(50))
        print(f"Bem vindo, {self.funcionario.get_nome()}!".center(50))
        print("=" * 60,"\n")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Veículo")
        print("3 - Cadastrar Funcionário")
        print("4 - Alterar Cliente")
        print("5 - Alterar Veículo")
        print("6 - Alterar Funcionário")
        print("7 - Excluir Cliente")
        print("8 - Excluir Veículo")
        print("9 - Excluir Funcionário")
        print("10 - Listar Clientes")
        print("11 - Listar Funcionários")
        print("12 - Listar Veículos Disponíveis")
        print("13 - Exibir veículos alugados por um cliente")
        print("14 - Exibir histórico de alugueis de um cliente")
        print("0 - Sair")
        print("="*60)

        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            self.cadastrar_Cliente()
            self.menu_Funcionario() #Para que o funcionário possa realizar mais de uma operação
        elif opcao == 2:
            self.cadastrar_Veiculo()
            self.menu_Funcionario()
        elif opcao == 3:
            if self.funcionario.get_cargo() == "Administrador":
                self.cadastrar_Funcionario()
                self.menu_Funcionario()
            else:
                print("Você não tem permissão para realizar essa operação")
                self.menu_Funcionario()
        elif opcao == 4:
            if self.funcionario.get_cargo() == "Administrador":
                self.alterar_Cliente()
            else:
                print("Você não tem permissão para realizar essa operação")
                self.menu_Funcionario()
        elif opcao == 5:
            if self.funcionario.get_cargo() == "Administrador":
                self.alterar_Funcionario()
            else:
                print("Você não tem permissão para realizar essa operação")
                self.menu_Funcionario()
        elif opcao == 6:
            if self.funcionario.get_cargo() == "Administrador":
                self.alterar_Veiculo()
            else:
                print("Você não tem permissão para realizar essa operação")
                self.menu_Funcionario()
        elif opcao == 7:
            if self.funcionario.get_cargo() == "Administrador":
                self.excluir_Cliente()
                self.menu_Funcionario()
            else:
                print("Você não tem permissão para realizar essa operação")
                self.menu_Funcionario()

        elif opcao == 8:
            if self.funcionario.get_cargo() == "Administrador":
                self.excluir_Funcionario()
                self.menu_Funcionario()
            else:
                print("Você não tem permissão para realizar essa operação")
                self.menu_Funcionario()
        elif opcao == 9:
            if self.funcionario.get_cargo() == "Administrador":
                self.excluir_Veiculo()
                self.menu_Funcionario()
            else:
                print("Você não tem permissão para realizar essa operação")
                self.menu_Funcionario()

        elif opcao == 10:
            self.exibir_Clientes()
            self.menu_Funcionario()
        elif opcao == 11:
            if self.funcionario.get_cargo() == "Administrador":
                self.exibir_Funcionarios()
                self.menu_Funcionario()
            else:
                print("Você não tem permissão para realizar essa operação")
                self.menu_Funcionario()
        elif opcao == 12:
            self.exibir_Veiculos()
            self.menu_Funcionario()
        elif opcao == 13:
            self.listar_Veiculos_Alugados_Cliente()
            self.menu_Funcionario()
        elif opcao == 14:
            self.exibir_historico_locacao_Cliente()
            self.menu_Funcionario()
        elif opcao == 0:
            self.menu()
        else:
            print("Opção inválida")
            self.menu_Funcionario()

    def login(self):
        id = input("Digite seu ID: ")
        senha = input("Digite sua senha: ")
        for cliente in self.lista_Clientes:
            if cliente.get_id_pessoa() == id and cliente.get_senha() == senha:
                self.cliente = cliente
                self.menu_Cliente()
        for funcionario in self.lista_Funcionarios:
            if funcionario.get_id_pessoa() == id and funcionario.get_senha() == senha:
                self.funcionario = funcionario
                self.menu_Funcionario()
        print("ID ou senha incorretos")
        self.menu()
###############################################################################################
### funções de locação de veículos utilizando a classe locacao ###:

    def alugar_Veiculo(self):
        id_veiculo = input("Digite o ID do veículo: ")
        # Procura o veículo na lista de veículos disponíveis
        for veiculo in self.lista_Veiculos_disponiveis:
            if veiculo.get_id_veiculo() == id_veiculo:
                id_cliente = input("Digite o seu ID: ")
                while id_cliente != self.cliente.get_id_pessoa():
                    id_cliente = input("ID incorreto. Digite o seu ID: ")
                # Procura o cliente na lista de clientes
                for cliente in self.lista_Clientes:
                    if cliente.get_id_pessoa() == id_cliente:
                        # Remove o veículo da lista de veículos disponíveis e adiciona na lista de veículos locados
                        self.lista_Veiculos_disponiveis.remove(veiculo)
                        self.lista_Veiculos_locados.append(veiculo)
                        # Atualiza o status do veículo para "Não"
                        veiculo.set_disponivel("Não")
                        dias = int(input("Digite a quantidade de dias que deseja alugar o veículo: "))
                        valor_total = veiculo.get_valor_diaria() * dias
                        # Cria uma nova locação
                        locacao = Locacao(cliente, veiculo, dias, valor_total)
                        # Adiciona a locação ao histórico do cliente
                        cliente.adicionar_historico_locacao(locacao)
                        cliente.adicionar_veiculo_alugado(veiculo)
                        print("Veículo alugado com sucesso!")
                        break
                break
        else:
            print("Veículo não encontrado.")

    def devolver_Veiculo(self):
        id_veiculo = input("Digite o ID do veículo: ")
        # Procura o veículo na lista de veículos locados
        for veiculo in self.lista_Veiculos_locados:
            if veiculo.get_id_veiculo() == id_veiculo:
                # Remove o veículo da lista de veículos locados e adiciona na lista de veículos disponíveis
                self.lista_Veiculos_locados.remove(veiculo)
                self.lista_Veiculos_disponiveis.append(veiculo)
                # Atualiza o status do veículo para "Sim"
                veiculo.set_disponivel("Sim")
                # Procura o cliente na lista de clientes
                for cliente in self.lista_Clientes:
                    if cliente.get_id_pessoa() == self.cliente.get_id_pessoa():
                        # Remove o veículo da lista de veículos alugados do cliente
                        cliente.remover_veiculo_alugado(veiculo)
                        print("Veículo devolvido com sucesso!")
                        break
                break
        else:
            print("Veículo não encontrado.")
            
    def listar_Veiculos_Alugados_Cliente(self):
        id_cliente = input("Digite o seu ID: ")
        for cliente in self.lista_Clientes:
            if cliente.get_id_pessoa() == id_cliente:
                # Verifica se o cliente possui veículos alugados
                if len (cliente.get_veiculos_alugados()) == 0:
                    print("Nenhum veículo alugado.")
                    break
                else:
                    print("=" * 50)
                    print("\nVeículos alugados: \n")
                    for veiculo in cliente.get_veiculos_alugados():
                        # Exibe os veículos alugados pelo cliente e seus valores com quebra de linha, id, modelo, marca, ano e valor da diária 
                        print("=" * 30)
                        print(f"ID: {veiculo.get_id_veiculo()}\nModelo: {veiculo.get_modelo()}\nMarca: {veiculo.get_marca()}\nAno: {veiculo.get_ano()}\nValor da diária: R$ {veiculo.get_valor_diaria()}\n")   
                        print("=" * 30)
                    print("=" * 50)
                    break
        else:
            print("ID incorreto.")
    
    def exibir_historico_locacao_Cliente(self):
        id_cliente = input("Digite o seu ID: ")
        for cliente in self.lista_Clientes:
            if cliente.get_id_pessoa() == id_cliente:
                # Verifica se o cliente possui histórico de locações
                if len (cliente.get_historico_locacao()) == 0:
                    print("Nenhuma locação registrada.")
                    break
                else:
                    print("=" * 50)
                    print("\nHistórico de locações: \n")
                    for locacao in cliente.get_historico_locacao():
                        # Exibe o histórico de locações do cliente com quebra de linha, id, modelo, marca, ano, valor da diária, dias, valor total
                        print("=" * 30)
                        print(f"ID: {locacao.get_veiculo().get_id_veiculo()}\nModelo: {locacao.get_veiculo().get_modelo()}\nMarca: {locacao.get_veiculo().get_marca()}\nAno: {locacao.get_veiculo().get_ano()}\nValor da diária: R$ {locacao.get_veiculo().get_valor_diaria()}\nDias: {locacao.get_dias()}\nValor total: R$ {locacao.get_valor_total()}\n")
                        print("=" * 30)
                    print("=" * 50)
                    break
        else:
            print("ID incorreto.")
    
    def menu_Cliente(self):
        print("=" * 60)
        print("Menu Cliente".center(50))
        print(f"Bem vindo, {self.cliente.get_nome()}!".center(50), "\n")
        print("=" * 60)
        print("1 - Alugar Veículo")
        print("2 - Devolver Veículo")
        print("3 - Listar Veículo Alugados")
        print("4 - Exibir Histórico de Locações")
        print("5 - Exibir Veículos disponíveis")
        print("0 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            self.alugar_Veiculo()
            self.menu_Cliente()
        elif opcao == 2:
            self.devolver_Veiculo()
            self.menu_Cliente()
        elif opcao == 3:
            self.listar_Veiculos_Alugados_Cliente()
            self.menu_Cliente()
        elif opcao == 4:
            self.exibir_historico_locacao_Cliente()
            self.menu_Cliente()
        elif opcao == 5:
            self.exibir_Veiculos()
            self.menu_Cliente()
        elif opcao == 0:
            self.menu()
        else:
            print("Opção inválida")
            self.menu_Cliente()
              
    
    def menu(self): # Menu inicial
        print("=" * 60)
        print("Fogaréu Rent de 30 de Fevereiro".center(60),"\n")
        print("1 - Login")
        print("2 - Cadastro")
        print("0 - Sair")
        print("=" * 60, "\n")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 0:
            print("Obrigado por utilizar o sistema de locação de automóveis")
            exit()
        elif opcao == 1:
            self.login()
        elif opcao == 2:
            self.cadastrar_Pessoa()
        else:
            print("Opção inválida")
            self.menu()
    


while True:
    main = Main()
    main.menu()



    





