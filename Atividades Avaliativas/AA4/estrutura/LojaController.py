from LojaModel import LojaModel

class LojaController:
    def __init__(self):
        self.model = LojaModel()

    # Funcionário
    def criar_funcionario(self, nome, cpf, id_funcionario, telefone, salario, cargo):
        self.model.criar_funcionario(nome, cpf, id_funcionario, telefone, salario, cargo)

    def obter_funcionario(self, id_funcionario):
        return self.model.obter_funcionario(id_funcionario)

    def atualizar_funcionario(self, id_funcionario, novo_nome, novo_cpf, novo_telefone, novo_salario, novo_cargo):
        return self.model.atualizar_funcionario(id_funcionario, novo_nome, novo_cpf, novo_telefone, novo_salario, novo_cargo)

    def deletar_funcionario(self, id_funcionario):
        return self.model.deletar_funcionario(id_funcionario)
    
    # Cliente
    def criar_cliente(self, cpf, nome, id_cliente, endereco, email, senha, historico_compras):
        self.model.criar_cliente(cpf, nome, id_cliente, endereco, email, senha, historico_compras)

    def obter_cliente(self, id_cliente):
        return self.model.obter_cliente(id_cliente)
    
    def atualizar_cliente(self, id_cliente, novo_cpf, novo_nome, novo_endereco, novo_email, nova_senha ):
        return self.model.atualizar_cliente(id_cliente, novo_cpf, novo_nome, novo_endereco, novo_email, nova_senha )
    
    def deletar_cliente(self, id_cliente):
        return self.model.deletar_cliente(id_cliente)
    
    # Produto
    def criar_produto(self, departamento, tipo, tamanho, genero, unidades, codigo_serial, preco):
        self.model.criar_produto(departamento, tipo, tamanho, genero, unidades, codigo_serial, preco)

    def obter_produto(self, codigo_serial):
        return self.model.obter_produto(codigo_serial)
    
    def atualizar_produto(self,codigo_serial,novo_departamento, novo_tipo, novo_tamanho, novo_genero, novo_unidades, novo_codigo_serial, novo_preco):
        return self.model.atualizar_produto(codigo_serial, novo_departamento, novo_tipo, novo_tamanho, novo_genero, novo_unidades, novo_codigo_serial, novo_preco) 

    def deletar_produto(self, codigo_serial):
        return self.model.deletar_produto(codigo_serial)
    
