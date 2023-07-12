class Compra:
    def __init__(self, id_compra, data_compra, valor_total, forma_pagamento, produtos):
        self.id_compra = id_compra
        self.data_compra = data_compra
        self.valor_total = valor_total
        self.forma_pagamento = forma_pagamento
        self.produtos = produtos # coleção de produtos comprados