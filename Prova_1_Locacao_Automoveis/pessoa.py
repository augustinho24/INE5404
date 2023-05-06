
class Pessoa:
    def __init__(self, nome, cpf,idade,id_pessoa,senha):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.id_pessoa = id_pessoa
        self.senha = senha  

    def get_nome(self):
        return self.nome
    def set_nome (self, nome):
        self.nome = nome
    
    def get_cpf(self):
        return self.cpf
    def set_cpf(self, cpf):
        self.cpf = cpf
    
    def get_idade(self):
        return self.idade
    def set_idade(self, idade):
        self.idade = idade
    
    def get_id_pessoa(self):
        return self.id_pessoa
    def set_id_pessoa(self, id_pessoa):
        self.id_pessoa = id_pessoa

    def get_senha(self):
        return self.senha
    def set_senha(self, senha):
        self.senha = senha
                
class Cliente(Pessoa):
    def __init__(self, nome, cpf, idade, id, senha, historico_locacao, veiculos_alugados):
        super().__init__(nome, cpf, idade, id, senha)
        self.historico_locacao = historico_locacao
        self.veiculos_alugados = veiculos_alugados

    def get_historico_locacao(self):
        return self.historico_locacao
    def set_historico_locacao(self, historico_locacao):
        self.historico_locacao = historico_locacao
    
    def get_veiculos_alugados(self):
        return self.veiculos_alugados
    def set_veiculos_alugados(self, veiculos_alugados):
        self.veiculos_alugados = veiculos_alugados

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, idade, id, senha, salario, cargo):
        super().__init__(nome, cpf, idade, id, senha)
        self.salario = salario
        self.cargo = cargo

    def get_salario(self):
        return self.salario
    def set_salario(self, salario):
        self.salario = salario
    
    def get_cargo(self):
        return self.cargo
    def set_cargo(self, cargo):
        self.cargo = cargo


 # Testando a classe
#pessoa = Pessoa("João", "123.456.789-10", 20, 1, "123")
#print(pessoa.get_nome())
#print(pessoa.get_cpf())
#print(pessoa.get_idade())
#print(pessoa.get_id_pessoa())
#print(pessoa.get_senha())












 
        