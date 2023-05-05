class Locadora_de_carros():
    def __init__(self):
        self.veiculos_disponiveis = []
        self.veiculos_alugados = []
        self.clientes = []
        self.funcionarios = []
        
    def set_veiculos_disponiveis(self, veiculo):
        self.veiculos_disponiveis.append(veiculo)
    def get_veiculos_disponiveis(self):
        return self.veiculos_disponiveis

    def set_veiculos_alugados(self, veiculo):
        self.veiculos_alugados.append(veiculo)
    def get_veiculos_alugados(self):
        return self.veiculos_alugados
        
    def set_clientes(self, cliente):
        self.clientes.append(cliente)
    def get_clientes(self):
        return self.clientes
        
    def set_locacoes(self, locacao):
        self.locacoes.append(locacao)
    def get_locacoes(self):
        return self.locacoes

    def set_funcionarios(self, funcionario):
        self.funcionarios.append(funcionario)
    def get_funcionarios(self):
        return self.funcionarios









 
 
    