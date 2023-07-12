# teste
class Cliente():
    def __init__(self, nome, rg, endereco, telefone, email, senha, historico_compras):
        self.nome = nome
        self.rg = rg
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.historico_compras = historico_compras
        
    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome

    def getRg(self):
        return self.rg
    def setRg(self, rg):
        self.rg = rg

    def getTelefone(self):
        return self.telefone
    def setTelefone(self, telefone):
        self.telefone = telefone

    def getEndereco(self):
        return self.endereco
    def setEndereco(self, endereco):
        self.endereco = endereco

    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email
        
    def getSenha(self):
        return self.senha
    def setSenha(self, senha):
        self.senha = senha

    def getHistoricoCompras(self):
        return self.historico_compras
    def setHistoricoCompras(self, historico_compras):
        self.historico_compras = historico_compras

    def getPreco(self):
        return self.preco
    def setPreco(self, preco):
        self.preco = preco

    def getFormaPagamento(self):
        return self.forma_pagamento
    def setFormaPagamento(self, forma_pagamento):
        self.forma_pagamento = forma_pagamento

    def getDesconto(self):
        return self.desconto
    def setDesconto(self, desconto):
        self.desconto = desconto
        
