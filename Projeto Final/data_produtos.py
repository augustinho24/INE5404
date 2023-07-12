class BD_Produtos:
    def __init__(self):
        self.conjunto_id_produtos = set() # Armaneza os ids dos produtos cadastrados
        self.lista_produtos = [] # Lista de produtos cadastrados

    
    def buscar_produto(self, id): # Busca produto pelo id
        for produto in self.lista_produtos:
            if produto.id_produto == id:
                return produto
        return None
    
    def pega_lista_clientes(self): # Retorna a lista de clientes
        return self.lista_clientes
    
    
    def verifica_id_produto(self, id): # Verifica se o id já está cadastrado
        if id in self.conjunto_id_produtos:
            return True
        else:
            return False
     
    def adicionar_produto(self, produto): # Adiciona produto na lista de produtos, no conjunto de ids de produtos e ordena a lista de produtos por ordem crescente pelo id
        self.lista_produtos.append(produto)
        self.conjunto_id_produtos.add(produto.id_produto)
        self.lista_produtos.sort(key=lambda x: x.id_produto)
        print("Produto adicionado com sucesso!")
    
    def remover_produto(self, id): # Remove produto da lista de produtos e do conjunto de ids de produtos
        for produto in self.lista_produtos:
            if produto.id_produto == id:
                self.lista_produtos.remove(produto)
                self.conjunto_id_produtos.remove(id)
                self.lista_produtos.sort(key=lambda x: x.id_produto)
                print("Produto removido com sucesso!")
                return True
        return False


    def atualizar_produto(self, id, novo_nome, novo_preco, nova_quantidade, novo_tipo_produto, novo_descricao, novo_eh_importado, novo_estado, novo_defeitos, novo_autor, novo_idioma, novo_editora, novo_data_publicacao, novo_qtd_paginas, novo_dimensoes, novo_isbn_10, novo_isbn_13, novo_edicao, novo_volume): # Atualiza produto
        produto = self.buscar_produto(id)
        if produto:
            produto.nome = novo_nome
            produto.preco = novo_preco
            produto.quantidade = nova_quantidade
            produto.tipo_produto = novo_tipo_produto
            produto.descricao = novo_descricao
            produto.eh_importado = novo_eh_importado
            produto.estado = novo_estado
            produto.defeitos = novo_defeitos
            produto.autor = novo_autor
            produto.idioma = novo_idioma
            produto.editora = novo_editora
            produto.data_publicacao = novo_data_publicacao
            produto.qtd_paginas = novo_qtd_paginas
            produto.dimensoes = novo_dimensoes
            produto.isbn_10 = novo_isbn_10
            produto.isbn_13 = novo_isbn_13
            produto.edicao = novo_edicao
            produto.volume = novo_volume
            print("Produto atualizado com sucesso!")
            return True
        print("Erro: produto não encontrado!")
        return False


    
      
        
    


    


    
    





    
    

       


