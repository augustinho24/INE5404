class Veiculo:
    def __init__(self, id_veiculo, placa, marca, modelo, ano, valor_diaria, qtd_portas, qtd_passageiros, cambio, disponivel):
        self.id_veiculo = id_veiculo
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
        self.qtd_portas = qtd_portas
        self.qtd_passageiros = qtd_passageiros
        self.cambio = cambio
        self.disponivel = disponivel   

    def get_id_veiculo(self):
        return self.id_veiculo
    def set_id_veiculo(self, id_veiculo):
        self.id_veiculo = id_veiculo
    
    def get_placa(self):
        return self.placa
    def set_placa(self, placa):
        self.placa = placa
    
    def get_marca(self):
        return self.marca
    def set_marca(self, marca):
        self.marca = marca
    
    def get_modelo(self):
        return self.modelo
    def set_modelo(self, modelo):
        self.modelo = modelo
    
    def get_ano(self):
        return self.ano
    def set_ano(self, ano):
        self.ano = ano
    
    def get_valor_diaria(self):
        return self.valor_diaria
    def set_valor_diaria(self, valor_diaria):
        self.valor_diaria = valor_diaria
    
    def get_qtd_portas(self):
        return self.qtd_portas
    def set_qtd_portas(self, qtd_portas):
        self.qtd_portas = qtd_portas
    
    def get_qtd_passageiros(self):
        return self.qtd_passageiros
    def set_qtd_passageiros(self, qtd_passageiros):
        self.qtd_passageiros = qtd_passageiros
    
    def get_cambio(self):
        return self.cambio
    def set_cambio(self, cambio):
        self.cambio = cambio
    
    def get_disponivel(self):
        return self.disponivel
    def set_disponivel(self, disponivel):
        self.disponivel = disponivel


