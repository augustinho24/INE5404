# Importando as classes
from pessoa import Pessoa, Cliente, Funcionario
from veiculo import Veiculo
from locacao import Locacao

class Main():
    def __init__(self):
        pass
    lista_Clientes = [] # Lista de clientes cadastrados
    lista_Funcionarios = [] # Lista de funcionarios cadastrados
    lista_Veiculos_disponiveis = [] # Lista de veiculos disponiveis para locação
    lista_Veiculos_locados = [] # Lista de veiculos locados/Alugados
    ids_cadastrados = set() # Para não haver repetição de senhas de pessoas
    senhas_cadastrados = set() # Para não haver repetição de ids de pessoas
    ids_veiculos_cadastrados = set() # Para não haver repetição de ids de veiculos
    mster_password = "agostinho carrara" # Chave para permitir o cadastro de funcionarios com o cargo de Administrador  


#### Funções de cadastro, alteração, remoção e listagem de Clientes, Funcionarios e Veiculos ####:

    def cadastrar_Veiculo(self): # Cadastra um veiculo na lista de veiculos disponiveis
        id_veiculo = input("Digite o id do veiculo: ")
        while id_veiculo in self.ids_veiculos_cadastrados or id_veiculo == '0':
            print("ID já cadastrado (inválido se for 0)")
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
    
    def alterar_Veiculo(self): # Altera um veiculo na lista de veiculos disponiveis
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
  
   
    def exibir_Veiculos(self): # Exibe todos os veiculos cadastrados
        print("=" * 50)
        print("Veiculos disponíveis:")
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
        print("=" * 50)


    def exibir_Veiculos_alugados(self): # Exibe todos os veiculos alugados ### COLOCAR NO MENU DE FUNCIONÁRIOS
        print("=" * 50)
        print("Veiculos alugados:")
        for veiculo in self.lista_Veiculos_locados:
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

    def excluir_Veiculo(self): # Exclui um veiculo da lista de veiculos disponiveis
        id_veiculo = input("Digite o id do veiculo: ")
        if id_veiculo not in self.ids_veiculos_cadastrados:
            print("ID não cadastrado\n")
            self.menu_Funcionario()
        for veiculo in self.lista_Veiculos_disponiveis:
            if veiculo.get_id_veiculo() == id_veiculo:
                self.lista_Veiculos_disponiveis.remove(veiculo)
                self.ids_veiculos_cadastrados.remove(id_veiculo)
                print("Remoção realizada com sucesso")
                self.menu_Funcionario()
                 # Volta para o menu principal    

    def cadastrar_Pessoa(self): # Função disponibilizada para o usuario escolher o tipo de cadastro, no qual invoca as funções de cadastro de cliente ou funcionário
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
        
    def cadastrar_Cliente(self): # Cadastra um cliente
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")
        idade = input("Digite sua idade: ")
        id = input("Digite um id: ")
        while id in self.ids_cadastrados or id == '0':
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
    
    def cadastrar_Funcionario(self): # Cadastra um funcionario
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")
        idade = input("Digite sua idade: ")
        id = input("Digite um id: ")
        while id in self.ids_cadastrados or id == '0':
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
            while chave != self.mster_password: # Verifica se a chave de acesso é igual a chave mestra, para permitir o cadastro de um administrador
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
  
    def exibir_Clientes(self): # Exibe os clientes cadastrados
        print("=" * 50)
        print("Clientes cadastrados: \n")
        for cliente in self.lista_Clientes:
            print("=" * 30)
            print("Nome: " ,cliente.get_nome())
            print("CPF:" ,cliente.get_cpf())
            print("Idade: " ,cliente.get_idade())
            print("ID:" ,cliente.get_id_pessoa())
            print("=" * 30)
        print("=" * 50)

    def exibir_Funcionarios(self): # Exibe os funcionarios cadastrados
        print("=" * 50)
        print("Funcionários cadastrados: \n")
        for funcionario in self.lista_Funcionarios:
            print("=" * 30)
            print("Nome: " ,funcionario.get_nome())
            print("CPF:" ,funcionario.get_cpf())
            print("Idade: " ,funcionario.get_idade())
            print("ID:" ,funcionario.get_id_pessoa())
            print("Salario: " ,funcionario.get_salario())
            print("Cargo: " ,funcionario.get_cargo())
            print("=" * 30)
        print("=" * 50)

    def alterar_Cliente(self): # Altera os dados de um cliente
        while True:
            id_cliente = input("Digite o id do cliente que deseja alterar: ")
            if id_cliente == '0':
                self.menu_Funcionario()
            while id_cliente not in self.ids_cadastrados:
                print("ID não cadastrado")
                id_cliente = input("Digite o id do cliente que deseja alterar: ")
                if id_cliente == '0':
                    self.menu_Funcionario()
            for cliente in self.lista_Clientes:
                if cliente.get_id_pessoa() == id_cliente:
                    print("O que deseja alterar? \n")
                    print("1 - Nome\n2 - CPF\n3 - Idade\n4 - Senha\n5 - Sair")
                    while True:
                        opcao = int(input("Digite a opção desejada: "))
                        if opcao == 1:
                            nome = input("Digite o novo nome: ")
                            cliente.set_nome(nome)
                        elif opcao == 2:
                            cpf = input("Digite o novo cpf: ")
                            cliente.set_cpf(cpf)
                        elif opcao == 3:
                            idade = input("Digite a nova idade: ")
                            cliente.set_idade(idade)
                        elif opcao == 4:
                            senha = input("Digite a nova senha: ")
                            while senha in self.senhas_cadastrados:
                                print("Senha já cadastrada")
                                senha = input("Digite uma senha: ")
                            cliente.set_senha(senha)
                        elif opcao == 5:
                            break
                        else:
                            print("Opção inválida")
                else:
                    print("Cliente não encontrado")
                    break
            break
        print("Alteração realizada com sucesso")
        self.menu_Funcionario()

    def alterar_Funcionario(self): # Altera os dados de um funcionario
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
            print("1 - Nome\n2 - CPF\n3 - Idade\n4 - Senha\n5 - Salario\n6 - Cargo\n7 - Sair")
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
                senha = input("Digite a nova senha: ")
                self.funcionario.set_senha(senha)
                while senha in self.senhas_cadastrados and senha != self.funcionario.get_senha():
                    print("Senha já cadastrada")
                    senha = input("Digite sua senha: ")
                #remover a senha da lista de senhas
                self.senhas_cadastrados.remove(self.funcionario.get_senha())
                self.funcionario.set_senha(senha)
            elif opcao == 5:
                salario = input("Digite o novo salario: ")
                self.funcionario.set_salario(salario)
            elif opcao == 6:
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
  
    
    def excluir_Cliente(self): # Exclui um cliente
        id = input("Digite o id do cliente que deseja excluir: ")
        for cliente in self.lista_Clientes:
            if cliente.get_id_pessoa() == id:
                self.lista_Clientes.remove(cliente)
                # remover o id da lista de ids
                self.ids_cadastrados.remove(cliente.get_id_pessoa())
                # remover a senha da lista de senhas
                self.senhas_cadastrados.remove(cliente.get_senha())
                print("Cliente excluído com sucesso")
                self.menu_Funcionario()
                return # sair do método após remover o cliente
            print("Cliente não encontrado")
            self.menu_Funcionario()

    
    def excluir_Funcionario(self): # Exclui um funcionario
        id = input("Digite o id do funcionario que deseja excluir: ")
        for funcionario in self.lista_Funcionarios:
            if funcionario.get_id_pessoa() == id:
                self.lista_Funcionarios.remove(funcionario)
                # remover o id da lista de ids
                self.ids_cadastrados.remove(funcionario.get_id_pessoa())
                # remover a senha da lista de senhas
                self.senhas_cadastrados.remove(funcionario.get_senha())
                print("Funcionário excluído com sucesso")
                self.menu_Funcionario()
                return # sair do método após remover o funcionário
        print("Funcionário não encontrado")
        self.menu_Funcionario()

### funções de locação de veículos utilizando a classe Locacao ###:

    def alugar_Veiculo(self): # Função para alugar um veículo
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
                        cliente.adicionar_historico_locacao(locacao) # Adiciona a locação ao histórico do cliente
                        cliente.adicionar_veiculo_alugado(veiculo) # Adiciona o veículo à lista de veículos alugados do cliente
                        print("Veículo alugado com sucesso!")
                        break
                break
        else:
            print("Veículo não encontrado.")

    def devolver_Veiculo(self): # Função para devolver um veículo
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
                        cliente.remover_veiculo_alugado(veiculo) # Remove o veículo da lista de veículos alugados do cliente
                        print("Veículo devolvido com sucesso!")
                        break
                break
        else:
            print("Veículo não encontrado.")
            
    def listar_Veiculos_Alugados_Cliente(self): # Função para listar os veículos alugados por um cliente
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
    
    def exibir_historico_locacao_Cliente(self): # Função para exibir o histórico de locações de um cliente
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

#### Login e menus ####:

    def login(self): # Realiza o login de um cliente ou funcionário
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

    def menu_Funcionario(self): # Menu do funcionario com as opções de cadastro, alteração e exclusão
        print("="*60)
        print("Menu Funcionário".center(50))
        print(f"Bem vindo, {self.funcionario.get_nome()}!".center(50))
        print("=" * 60,"\n")
        print("0 - Sair")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Veículo")
        print("3 - Cadastrar Funcionário")
        print("4 - Alterar Cliente")
        print("5 - Alterar Funcionario")
        print("6 - Alterar Veículo")
        print("7 - Excluir Cliente")
        print("8 - Excluir Funcionário")
        print("9 - Excluir Veículo")
        print("10 - Listar Clientes")
        print("11 - Listar Funcionários")
        print("12 - Listar Veículos Disponíveis")
        print("13 - Listar Veículos Alugados")
        print("14 - Listar Veículos Alugados por Cliente")
        print("15 - Exibir Histórico de Locações de um Cliente")
        print("=" * 60, "\n")

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
                self.menu_Funcionario()
            else:
                print("Você não tem permissão para realizar essa operação")
                self.menu_Funcionario()
        elif opcao == 5:
            if self.funcionario.get_cargo() == "Administrador":
                self.alterar_Funcionario()
                self.menu_Funcionario()
            else:
                print("Você não tem permissão para realizar essa operação")
                self.menu_Funcionario()
        elif opcao == 6:
            if self.funcionario.get_cargo() == "Administrador":
                self.alterar_Veiculo()
                self.menu_Funcionario()
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
            self.exibir_Veiculos_alugados()
            self.menu_Funcionario()
        elif opcao == 14:
            self.listar_Veiculos_Alugados_Cliente()
            self.menu_Funcionario()
        elif opcao == 15:
            self.exibir_historico_locacao_Cliente()
            self.menu_Funcionario()
        elif opcao == 0:
            self.menu()
        else:
            print("Opção inválida\n")
            self.menu_Funcionario()
    
    def menu_Cliente(self): # Função para exibir o menu do cliente
        print("=" * 60)
        print("Menu Cliente".center(50))
        print(f"Bem vindo, {self.cliente.get_nome()}!".center(50), "\n")
        print("=" * 60)
        print("1 - Alugar Veículo")
        print("2 - Devolver Veículo")
        print("3 - Listar seus Veículos alugados")
        print("4 - Exibir Histórico de Locações")
        print("5 - Exibir Veículos disponíveis")
        print("0 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            self.alugar_Veiculo()
            self.menu_Cliente() # Volta para o menu do cliente
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
            self.menu() # Volta para o menu inicial
        else:
            print("Opção inválida\n")
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
            print("Obrigado por utilizar o sistema de Locação de Automóveis de Fogaréu Rent de 30 de Fevereiro!")
            exit() # Finaliza o programa
        elif opcao == 1:
            self.login()
        elif opcao == 2:
            self.cadastrar_Pessoa() # Chama a função para cadastrar uma pessoa, que pode ser um cliente ou um funcionário
        else:
            print("Opção inválida\n")
            self.menu()
    


while True:
    main = Main() # Instancia a classe Main
    main.menu() # Chama a função menu, que inicia o programa



    





