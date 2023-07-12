class Locacao:
    def __init__(self, cliente, veiculo, dias, valor_total):
        self.cliente = cliente
        self.veiculo = veiculo
        self.dias = dias
        self.valor_total = valor_total

    def get_cliente(self):
        return self.cliente
    def set_cliente(self, cliente):
        self.cliente = cliente
    
    def get_veiculo(self):
        return self.veiculo
    def set_veiculo(self, veiculo):
        self.veiculo = veiculo
    
    def get_dias(self):
        return self.dias
    def set_dias(self, dias):
        self.dias = dias

    def get_valor_total(self):
        return self.valor_total
    def set_valor_total(self, valor_total):
        self.valor_total = valor_total
    
        
    



