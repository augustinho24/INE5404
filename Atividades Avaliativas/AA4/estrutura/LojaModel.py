class Funcionario:
    def __init__(self, nome, cpf, id_funcionario, telefone, salario, cargo):
        self.nome = nome
        self.cpf = cpf
        self.id_funcionario = id_funcionario
        self.telefone = telefone
        self.salario = salario
        self.cargo = cargo

class Cliente:
    def __init__(self, cpf, nome, id_cliente, endereco, email, senha, historico_compras):
        self.cpf = cpf
        self.nome = nome
        self.id_cliente = id_cliente
        self.endereco = endereco
        self.email = email
        self.senha = senha
        self.historico_compras = historico_compras

class Produto():
    def __init__(self, departamento, tipo, tamanho, genero, unidades, codigo_serial, preco):
        self.departamento = departamento
        self.tipo = tipo
        self.tamanho = tamanho
        self.genero = genero
        self.unidades = unidades
        self.codigo_serial = codigo_serial
        self.preco = preco
 
class LojaModel:
    def __init__(self):
        self.funcionarios = []
        self.clientes = []
        self.produtos = []

    # Funcionário
    def criar_funcionario(self, nome, cpf, id_funcionario, telefone, salario, cargo):
        funcionario = Funcionario(nome, cpf, id_funcionario, telefone, salario, cargo)
        self.funcionarios.append(funcionario)

    def obter_funcionario(self, id_funcionario):
        for funcionario in self.funcionarios:
            if funcionario.id_funcionario == id_funcionario:
                return funcionario
        return None

    def atualizar_funcionario(self, id_funcionario, novo_nome, novo_cpf, novo_telefone, novo_salario, novo_cargo):
        funcionario = self.obter_funcionario(id_funcionario)
        if funcionario:
            funcionario.nome = novo_nome
            funcionario.cpf = novo_cpf
            funcionario.telefone = novo_telefone
            funcionario.salario = novo_salario
            funcionario.cargo = novo_cargo
            return True
        return False

    def deletar_funcionario(self, id_funcionario):
        funcionario = self.obter_funcionario(id_funcionario)
        if funcionario:
            self.funcionarios.remove(funcionario)
            return True
        return False

    # Cliente
    def criar_cliente(self, cpf, nome, id_cliente, endereco, email, senha, historico_compras):
        cliente = Cliente(cpf, nome, id_cliente, endereco, email, senha, historico_compras)
        self.clientes.append(cliente)

    def obter_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None

    def atualizar_cliente(self, id_cliente, novo_cpf, novo_nome, novo_endereco, novo_email, nova_senha ):
        cliente = self.obter_cliente(id_cliente)
        if cliente:
            cliente.cpf = novo_cpf
            cliente.nome = novo_nome
            cliente.endereco = novo_endereco
            cliente.email = novo_email
            cliente.senha = nova_senha
            return True
        return False

    def deletar_cliente(self, id_cliente):
        cliente = self.obter_cliente(id_cliente)
        if cliente:
            self.clientes.remove(cliente)
            return True
        return False

    # Produto
    def criar_produto(self, departamento, tipo, tamanho, genero, unidades, codigo_serial, preco):
        produto = Produto(departamento, tipo, tamanho, genero, unidades, codigo_serial, preco)
        self.produtos.append(produto)

    def obter_produto(self, codigo_serial):
        for produto in self.produtos:
            if produto.codigo_serial == codigo_serial:
                return produto
        return None
                        
    def atualizar_produto(self, codigo_serial, novo_departamento, novo_tipo, novo_tamanho, novo_genero, novo_unidades, novo_codigo_serial, novo_preco):
        produto = self.obter_produto(codigo_serial)
        if produto:
            produto.departamento = novo_departamento
            produto.tipo = novo_tipo
            produto.tamanho = novo_tamanho
            produto.genero = novo_genero
            produto.unidades = novo_unidades
            produto.codigo_serial = novo_codigo_serial
            produto.preco = novo_preco
            return True
        return False

    def deletar_produto(self, codigo_serial):
        produto = self.obter_produto(codigo_serial)
        if produto:
            self.produtos.remove(produto)
            return True
        return False
