class Produto:
    def __init__(self, id_produto, nome, preco, quantidade, tipo_produto, descricao, eh_importado, estado, defeitos, autor, idioma, editora, data_publicacao, qtd_paginas, dimensoes, isbn_10, isbn_13, edicao, volume):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.tipo_produto = tipo_produto
        self.descricao = descricao
        self.eh_importado = eh_importado
        self.estado = estado
        self.defeitos = defeitos
        self.autor = autor
        self.idioma = idioma
        self.editora = editora
        self.data_publicacao = data_publicacao
        self.qtd_paginas = qtd_paginas
        self.dimensoes = dimensoes
        self.isbn_10 = isbn_10
        self.isbn_13 = isbn_13
        self.edicao = edicao
        self.volume = volume



#class Compra:
#    def __init__(self, id_compra, data_compra, valor_total, forma_pagamento, produtos):
#        self.id_compra = id_compra
#        self.data_compra = data_compra
#        self.valor_total = valor_total
#        self.forma_pagamento = forma_pagamento
#        self.produtos = produtos # lista de produtos comprados
#


   