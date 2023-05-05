from locadora_carros import Locadora_de_carros
from veiculo import Veiculo

locadora_inst = Locadora_de_carros()
veiculo_inst = Veiculo()


class Pessoa():
    def __init__(self, id='', nome='', cpf=0, idade=0, telefone=0, senha='', usuario='', tipo_cadastro=''):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.tipo_cadastro = ''
        self.idade = idade
        self.telefone = telefone
        self.usuario = usuario
        self.senha = senha
        self.tipo_cadastro = tipo_cadastro

    
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome
    
    def get_cpf(self):
        return self.cpf
    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_tipo_cadastro(self):
        return self.tipo_cadastro
    def set_tipo_cadastro(self, tipo_cadastro):
        self.tipo_cadastro = tipo_cadastro
    
    def get_idade(self):
        return self.idade
    def set_idade(self, idade):
        self.idade = idade
    
    def get_telefone(self):
        return self.telefone
    def set_telefone(self, telefone):
        self.telefone = telefone
    
    def get_usuario(self):
        return self.usuario
    def set_usuario(self, usuario):
        self.usuario = usuario
    
    def get_senha(self):
        return self.senha
    def set_senha(self, senha):
        self.senha = senha


    

class Cliente(Pessoa):
    def __init__(self, id, nome, cpf, idade, telefone, senha, usuario):
        super().__init__(id, nome, cpf, idade, telefone, senha, usuario)
        self.tipo_cadastro = 'Cliente'
        self.veiculos_alugados_cliente = []

    def get_veiculos_alugados_cliente(self):
        return self.veiculos_alugados_cliente
    def set_veiculos_alugados_cliente(self, veiculo):
        self.veiculos_alugados_cliente.append(veiculo)
    
    def get_tipo_cadastro(self):
        return self.tipo_cadastro
    def set_tipo_cadastro(self, tipo_cadastro):
        self.tipo_cadastro = tipo_cadastro
    

class Funcionario(Pessoa):
    def __init__(self, id, nome, cpf, idade, telefone, senha, salario):
        super().__init__(id, nome, cpf, idade, telefone, senha)
        self.tipo_cadastro = 'Funcionario'
        self.cargo = ''
        self.salario = salario
    
    def get_cargo(self):
        return self.cargo
    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_salario(self):
        return self.salario
    def set_salario(self, salario):
        self.salario = salario
    
    def get_tipo_cadastro(self):
        return self.tipo_cadastro
    def set_tipo_cadastro(self, tipo_cadastro):
        self.tipo_cadastro = tipo_cadastro
    

class Gerente_geral(Funcionario):
    def __init__(self, id, nome, cpf, idade, telefone, senha, salario):
        super().__init__(id, nome, cpf, idade, telefone, senha, salario)
        self.cargo = 'Gerente Geral'

class Operador(Funcionario):
    def __init__(self, id, nome, cpf, idade, telefone, senha, salario):
        super().__init__(id, nome, cpf, idade, telefone, senha, salario)
        self.cargo = 'Operador'

class Administrador_sistema(Funcionario):
    def __init__(self, id, nome, cpf, idade, telefone, senha, salario):
        super().__init__(id, nome, cpf, idade, telefone, senha, salario)
        self.cargo = 'Administrador do Sistema'


def cadastro_Pessoa():
    print('Cadastro de Pessoa')
    id = input('Digite o ID: ')
    nome = input('Digite o nome: ')
    cpf = int(input('Digite o CPF: '))
    idade = int(input('Digite a idade: '))
    while idade < 18:
        idade = int(input('Idade inválida. Digite novamente: '))
    telefone = int(input('Digite o telefone: '))
    senha = input('Digite a senha: ')
    usuario = input('Digite o usuário: ')
    tipo_cadastro = input('Digite o tipo de cadastro: \n1 - Cliente\n2 - Funcionário')
    while tipo_cadastro != '1' and tipo_cadastro != '2':
        tipo_cadastro = input('Tipo de cadastro inválido. Digite novamente: \n1 - Cliente\n2 - Funcionário')
    if tipo_cadastro == '1':
        cliente = Cliente(id, nome, cpf, idade, telefone, senha, usuario)
        locadora_inst.set_clientes(cliente)
    elif tipo_cadastro == '2':
        salario = float(input('Digite o salário: '))
        cargo = input('Digite o cargo: \n1 - Gerente Geral\n2 - Operador\n3 - Administrador do Sistema')
        while cargo != '1' and cargo != '2' and cargo != '3':
            cargo = input('Cargo inválido. Digite novamente: \n1 - Gerente Geral\n2 - Operador\n3 - Administrador do Sistema')
        if cargo == '1':
            funcionario = Gerente_geral(id, nome, cpf, idade, telefone, senha, salario)
            locadora_inst.set_funcionarios(funcionario)
        elif cargo == '2':
            funcionario = Operador(id, nome, cpf, idade, telefone, senha, salario)
            locadora_inst.set_funcionarios(funcionario)
        elif cargo == '3':
            funcionario = Administrador_sistema(id, nome, cpf, idade, telefone, senha, salario)
            locadora_inst.set_funcionarios(funcionario)

    print('Cadastro realizado com sucesso!')

def alterar_pessoa():
    tipo_cadastro = int(input('Digite o tipo de cadastro: \n1 - Cliente\n2 - Funcionário'))
    while tipo_cadastro != 1 and tipo_cadastro != 2:
        tipo_cadastro = int(input('Tipo de cadastro inválido. Digite novamente: \n1 - Cliente\n2 - Funcionário'))
    if tipo_cadastro == 1:
        id = input('Digite o ID do cliente: ')
        for cliente in locadora_inst.get_clientes():
            if cliente.get_id() == id:
                print('Dados atuais:')
                print(f'ID: {cliente.get_id()}')
                print(f'Nome: {cliente.get_nome()}')
                print(f'CPF: {cliente.get_cpf()}')
                print(f'Idade: {cliente.get_idade()}')
                print(f'Telefone: {cliente.get_telefone()}')
                print(f'Senha: {cliente.get_senha()}')
                print(f'Usuário: {cliente.get_usuario()}')
                print('------------------------------------')
                print('1 - Alterar nome \n2 - Alterar CPF \n3 - Alterar idade \n4 - Alterar telefone \n5 - Alterar senha \n6 - Alterar usuário \n 0 - Sair')
                opcao = int(input('Digite a opção desejada: '))
                while opcao !=0:
                    while opcao < 1 or opcao > 6:
                        opcao = int(input('Opção inválida. Digite novamente: '))
                    if opcao == 1:
                        novo_nome = input('Digite o novo nome: ')
                        cliente.set_nome(novo_nome)
                    elif opcao == 2:
                        novo_cpf = int(input('Digite o novo CPF: '))
                        cliente.set_cpf(novo_cpf)
                    elif opcao == 3:
                        nova_idade = int(input('Digite a nova idade: '))
                        while nova_idade < 18:
                            nova_idade = int(input('Idade inválida. Digite novamente: '))
                        cliente.set_idade(nova_idade)
                    elif opcao == 4:
                        novo_telefone = int(input('Digite o novo telefone: '))
                        cliente.set_telefone(novo_telefone)
                    elif opcao == 5:
                        nova_senha = input('Digite a nova senha: ')
                        cliente.set_senha(nova_senha)
                    elif opcao == 6:
                        novo_usuario = input('Digite o novo usuário: ')
                        cliente.set_usuario(novo_usuario)
                    print('Dados atualizados:')
                    print(f'ID: {cliente.get_id()}')
                    print(f'Nome: {cliente.get_nome()}')
                    print(f'CPF: {cliente.get_cpf()}')
                    print(f'Idade: {cliente.get_idade()}')
                    print(f'Telefone: {cliente.get_telefone()}')
                    print(f'Senha: {cliente.get_senha()}')
                    print(f'Usuário: {cliente.get_usuario()}')
                    print('------------------------------------')

    elif tipo_cadastro == 2:
        id = input('Digite o ID do funcionário: ')
        for funcionario in locadora_inst.get_funcionarios():
            if funcionario.get_id() == id:
                print('Dados atuais:')
                print(f'ID: {funcionario.get_id()}')
                print(f'Nome: {funcionario.get_nome()}')
                print(f'CPF: {funcionario.get_cpf()}')
                print(f'Idade: {funcionario.get_idade()}')
                print(f'Telefone: {funcionario.get_telefone()}')
                print(f'Salário: R$ {funcionario.get_salario()}')
                print(f'Cargo: {funcionario.get_cargo()}')
                print('------------------------------------')
                print('1 - Alterar nome \n2 - Alterar CPF \n3 - Alterar idade \n4 - Alterar telefone \n5 - Alterar salário \n6 - Alterar cargo \n 0 - Sair')
                opcao = int(input('Digite a opção desejada: '))
                while opcao !=0:
                    while opcao < 1 or opcao > 6:
                        opcao = int(input('Opção inválida. Digite novamente: '))
                    if opcao == 1:
                        novo_nome = input('Digite o novo nome: ')
                        funcionario.set_nome(novo_nome)
                    elif opcao == 2:
                        novo_cpf = int(input('Digite o novo CPF: '))
                        funcionario.set_cpf(novo_cpf)
                    elif opcao == 3:
                        nova_idade = int(input('Digite a nova idade: '))
                        while nova_idade < 18:
                            nova_idade = int(input('Idade inválida. Digite novamente: '))
                        funcionario.set_idade(nova_idade)
                    elif opcao == 4:
                        novo_telefone = int(input('Digite o novo telefone: '))
                        funcionario.set_telefone(novo_telefone)
                    elif opcao == 5:
                        novo_salario = float(input('Digite o novo salário: '))
                        funcionario.set_salario(novo_salario)
                    elif opcao == 6:
                        print(('------------------------------------'))
                        opcao = int(input('Digite o cargo: \n1 - Gerente Geral\n2 - Operador\n3 - Administrador do Sistema\n Digite o número correspondente ao cargo: '))
                        while opcao < 1 or opcao > 3:
                            opcao = int(input('Cargo inválido. Digite novamente: '))
                        if opcao == '1':
                            novo_cargo = 'Gerente Geral'
                        elif opcao == '2':
                            novo_cargo = 'Operador'
                        elif opcao == '3':
                            novo_cargo = 'Administrador do Sistema'
                        funcionario.set_cargo(novo_cargo)
                    print('Dados atualizados:')
                    print(f'ID: {funcionario.get_id()}')
                    print(f'Nome: {funcionario.get_nome()}')
                    print(f'CPF: {funcionario.get_cpf()}')
                    print(f'Idade: {funcionario.get_idade()}')
                    print(f'Telefone: {funcionario.get_telefone()}')
                    print(f'Salário: R$ {funcionario.get_salario()}')
                    print(f'Cargo: {funcionario.get_cargo()}')
                    print('------------------------------------')
                         
def listar_funcionarios():
    print('Funcionários cadastrados:')
    for funcionario in locadora_inst.get_funcionarios():
        print(f'ID: {funcionario.get_id()}')
        print(f'Nome: {funcionario.get_nome()}')
        print(f'CPF: {funcionario.get_cpf()}')
        print(f'Idade: {funcionario.get_idade()}')
        print(f'Telefone: {funcionario.get_telefone()}')
        print(f'Salário: R$ {funcionario.get_salario()}')
        print(f'Cargo: {funcionario.get_cargo()}')
        print('------------------------------------')

def listar_clientes():
    print('Clientes cadastrados:')
    for cliente in locadora_inst.get_clientes():
        print(f'ID: {cliente.get_id()}')
        print(f'Nome: {cliente.get_nome()}')
        print(f'CPF: {cliente.get_cpf()}')
        print(f'Idade: {cliente.get_idade()}')
        print(f'Telefone: {cliente.get_telefone()}')
        print(f'Usuário: {cliente.get_usuario()}')
        print('------------------------------------')

def remover_cliente():
    id = input('Digite o ID do cliente: ')
    for cliente in locadora_inst.get_clientes():
        if cliente.get_id() == id:
            locadora_inst.get_clientes().remove(cliente)
            print('Cliente removido com sucesso!')
            break
    else:
        print('Cliente não encontrado!')

def remover_funcionario():
    id = input('Digite o ID do funcionário: ')
    for funcionario in locadora_inst.get_funcionarios():
        if funcionario.get_id() == id:
            locadora_inst.get_funcionarios().remove(funcionario)
            print('Funcionário removido com sucesso!')
            break
    else:
        print('Funcionário não encontrado!')

def login():
    tipo_usuario = int(input('Digite o tipo de usuário: \n1 - Cliente\n2 - Funcionário\nDigite o número correspondente ao tipo de usuário: '))
    while tipo_usuario < 1 or tipo_usuario > 2:
        tipo_usuario = int(input('Tipo de usuário inválido. Digite novamente: '))
    if tipo_usuario == 1:
        usuario = input('Digite o usuário: ')
        senha = input('Digite a senha: ')
        for cliente in locadora_inst.get_clientes():
            if cliente.get_usuario() == usuario and cliente.get_senha() == senha:
                print('Login efetuado com sucesso!')
                menu_cliente(cliente)
                break
        else:  
            print('Usuário ou senha incorretos!')
    elif tipo_usuario == 2:
        usuario = input('Digite o usuário: ')
        senha = input('Digite a senha: ')
        for funcionario in locadora_inst.get_funcionarios():
            if funcionario.get_usuario() == usuario and funcionario.get_senha() == senha:
                print('Login efetuado com sucesso!')
                menu_funcionario(funcionario)
                break
        else:  
            print('Usuário ou senha incorretos!')

def menu_cliente(cliente):
    print('------------------------------------')
    print('1 - Alugar carro\n2 - Devolver carro\n3 - Listar carros disponíveis\n4-Listar seus veiculos alugados\n0 - Sair')
    opcao = int(input('Digite a opção desejada: '))
    while opcao != 0:
        while opcao < 1 or opcao > 4:
            opcao = int(input('Opção inválida. Digite novamente: '))
        if opcao == 1:
            alugar_veiculo(cliente)
        elif opcao == 2:
            devolver_veiculo(cliente)
        elif opcao == 3:
            veiculo_inst.listar_veiculos()
        elif opcao == 4:
            cliente.listar_veiculos_alugados()
        print('------------------------------------')

def alugar_veiculo(cliente):
    id_funcionario = input('ID do OPERADOR(A): ')
    for funcionario in locadora_inst.get_funcionarios():
        while funcionario.get_id() != id_funcionario or funcionario.get_cargo() != 'Operador':
            print('OPERADOR(A) não encontrado(a)!')
            id_funcionario = input('Digite o ID novamente: ')
        if funcionario.get_id() == id_funcionario and funcionario.get_cargo() == 'Operador':
            print('OPERADOR(A) encontrado(a)!')
        id_veiculo = int(input('ID do veículo: '))
        for veiculo in locadora_inst.get_veiculos_disponiveis():
            if veiculo.get_id_veiculo() == id_veiculo:
                veiculo.set_disponivel(False)
                locadora_inst.get_veiculos_disponiveis().remove(veiculo)
                locadora_inst.set_veiculos_alugados(veiculo)
                #adicionar veiculo na lista de veiculos alugados do cliente
                cliente.set_veiculos_alugados(veiculo)
                print('Veículo alugado com sucesso!')
                break
    else:
        print('Veículo não encontrado!')

def devolver_veiculo(cliente):
    id_veiculo = int(input('ID do veículo: '))
    for veiculo in locadora_inst.get_veiculos_alugados():
        if veiculo.get_id_veiculo() == id_veiculo:
            veiculo.set_disponivel(True)
            locadora_inst.get_veiculos_alugados().remove(veiculo)
            locadora_inst.set_veiculos_disponiveis(veiculo)
            #remover veiculo da lista de veiculos alugados do cliente
            cliente.get_veiculos_alugados().remove(veiculo)
            print('Veículo devolvido com sucesso!')
            break
    else:
        print('Veículo não encontrado!')
    

def listar_veiculos_alugados_cliente(cliente):
    print('Veículos alugados:')
    for veiculo in cliente.get_veiculos_alugados():
        print(f'ID: {veiculo.get_id_veiculo()}')
        print(f'Nome: {veiculo.get_nome()}')
        print(f'Placa: {veiculo.get_placa()}')
        print(f'Ano: {veiculo.get_ano()}')
        print(f'Cor: {veiculo.get_cor()}')
        print(f'Valor da diária: R$ {veiculo.get_valor_diaria()}')
        print('------------------------------------')

def menu_funcionario(funcionario):
    print('------------------------------------')
    print('1 - Cadastrar veículo\n2 - Remover veículo\n3 - Listar veículos\n4 - Cadastrar uma conta (Cliente ou Funcionário)\n5 - Remover cliente\n6 - Listar clientes\n7 - Remover Funcionário\n0 - Sair')
    opcao = int(input('Digite a opção desejada: '))
    while opcao != 0:
        while opcao < 1 or opcao > 6:
            opcao = int(input('Opção inválida. Digite novamente: '))
        if opcao == 1:
            #Restrito apenas para funcionários do cargo de Administrador do Sistema e Gerente Geral
            if funcionario.get_cargo() == 'Administrador do Sistema' or funcionario.get_cargo() == 'Gerente Geral':
                veiculo_inst.cadastrar_veiculo()
            else:
                print('Você não tem permissão para realizar essa operação!')
        elif opcao == 2:
            #Restrito apenas para funcionários do cargo de Administrador do Sistema e Gerente Geral
            if funcionario.get_cargo() == 'Administrador do Sistema' or funcionario.get_cargo() == 'Gerente Geral':
                veiculo_inst.remover_veiculo()
            else:
                print('Você não tem permissão para realizar essa operação!')
        elif opcao == 3:
            veiculo_inst.listar_veiculos()
        elif opcao == 4:
            cadastro_Pessoa()
        elif opcao == 5:
            #Restrito apenas para funcionários do cargo de Administrador do Sistema e Gerente Geral
            if funcionario.get_cargo() == 'Administrador do Sistema' or funcionario.get_cargo() == 'Gerente Geral':
                remover_cliente()
            else:
                print('Você não tem permissão para realizar essa operação!')            
        elif opcao == 6:
            listar_clientes()
        elif opcao == 7:
            #Restrito apenas para funcionários do cargo de Administrador do Sistema
            if funcionario.get_cargo() == 'Administrador do Sistema':
                remover_funcionario()
            else:
                print('Você não tem permissão para realizar essa operação!')

        print('------------------------------------')



            
            
     


            


        
    




    





 





