class Produto():
    def __init__(self, departamento, tipo, tamanho, genero, unidades, codigo_serial, preco):
        self.departamento = departamento
        self.tipo = tipo
        self.tamanho = tamanho
        self.genero = genero
        self.unidades = unidades
        self.codigo_serial = codigo_serial
        self.preco = preco   

    def getListaProdutos(self):
        return self.listaProdutos
    def setListaProdutos(self, listaProdutos):
        self.listaProdutos = listaProdutos

    def getDepartamento(self):
        return self.departamento
    def setDepartamento(self, departamento):
        self.departamento = departamento

    def getTipo(self):
        return self.tipo
    def setTipo(self, tipo):
        self.tipo = tipo

    def getTamanho(self):
        return self.tamanho
    def setTamanho(self, tamanho):
        self.tamanho = tamanho

    def getGenero(self):
        return self.genero
    def setGenero(self, genero):
        self.genero = genero

    def getUnidades(self):
        return self.unidades
    def setUnidades(self, unidades):
        self.unidades = unidades
    
    def getCodigoSerial(self):
        return self.codigo_serial
    def setCodigoSerial(self, codigo_serial):
        self.codigo_serial = codigo_serial
        
    def getPreco(self):
        return self.preco
    def setPreco(self, preco):
        self.preco = preco

class Compra(Produto):
    def __init__(self, departamento, tipo, tamanho, genero, unidades, codigo_serial, preco, forma_pagamento, desconto, total):
        super().__init__(departamento, tipo, tamanho, genero, unidades, codigo_serial, preco)
        self.forma_pagamento = forma_pagamento
        self.desconto = desconto
        self.total = total

    def getFormaPagamento(self):
        return self.forma_pagamento
    def setFormaPagamento(self, forma_pagamento):
        self.forma_pagamento = forma_pagamento

    def getDesconto(self):
        return self.desconto
    def setDesconto(self, desconto):
        self.desconto = desconto
    
    def getTotal(self):
        return self.total
    def setTotal(self, total):
        self.total = total
