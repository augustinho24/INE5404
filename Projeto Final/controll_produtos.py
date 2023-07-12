from data_produtos import BD_Produtos
from model_produto import Produto
class Controller_BD_produtos:
    def __init__(self):
        self.bd_produtos = BD_Produtos()


    def pega_lista_produtos(self): # Retorna a lista de produtos 
        return self.bd_produtos.lista_produtos

    def quebrar_linhas(self, texto, largura_maxima): # função para quebrar linhas de uma string
        palavras = texto.split()
        linhas = []
        linha_atual = ""

        for palavra in palavras:
            if len(linha_atual) + len(palavra) <= largura_maxima:
                linha_atual += palavra + " "
            else:
                linhas.append(linha_atual.strip())
                linha_atual = palavra + " "

        linhas.append(linha_atual.strip())
        return "\n".join(linhas)

    def cadastrar_produto(self): # função para cadastrar produto
        while True:
            try:
                id = int(input("Id do produto: "))
                while self.bd_produtos.verifica_id_produto(id):
                    print("Erro: Id já cadastrado!")
                    id = int(input("Id do produto: "))
                break
            except ValueError:
                print("Erro: Id inválido!")

        nome = input("Nome do produto: ")

        while True:
            try:
                preco = float(input("Preço do produto: "))
                break
            except ValueError:
                print("Erro: Preço inválido!")
        
        while True:
            try:
                quantidade = int(input("Quantidade do produto: "))
                break
            except ValueError:
                print("Erro: Quantidade inválida!")
        while True:
            try:
                opcao = int(input("Tipo do produto: (1 - Livro | 2 - HQ | 3 - Manga | 4 - Box) "))
                while opcao < 1 or opcao > 5:
                    print("Erro: Opção inválida!")
                    opcao = int(input("Tipo do produto: (1 - Livro | 2 - HQ | 3 - Manga | 4 - Box ): "))
                if opcao == 1:
                    tipo_produto = "Livro"
                elif opcao == 2:
                    tipo_produto = "HQ"
                elif opcao == 3:
                    tipo_produto = "Manga"
                elif opcao == 4:
                    tipo_produto = "Box"
                break
            except ValueError:
                print("Erro: Opção inválida!")

        descricao = input("Descrição do produto: ")
        if descricao == "":
            descricao = "Sem descrição"
        else:
            descricao = self.quebrar_linhas(descricao, 50)
        
        while True:
            try:
                eh_importado = int(input("O produto é importado? (1 - Sim | 0 - Não): "))
                while eh_importado < 0 or eh_importado > 1:
                    print("Erro: Opção inválida!")
                    eh_importado = int(input("O produto é importado? (1 - Sim | 0 - Não): "))
                if eh_importado == 1:
                    eh_importado = True
                elif eh_importado == 0:
                    eh_importado = False
                break
            except ValueError:
                print("Erro: Opção inválida!")
        try:
            opcao = int(input("Estado do produto: (1 - Novo | 2 - Usado): "))
        except ValueError:
                print("Erro: Opção inválida!")

        while opcao < 1 or opcao > 2:
            print("Erro: Opção inválida!")
            opcao = int(input("Estado do produto: (1 - Novo | 2 - Usado): "))
        if opcao == 1:
            estado = "Novo"
        elif opcao == 2:
            estado = "Usado"

        defeitos = input("Defeitos do produto: ")
        if defeitos == "":
            defeitos = "Sem descrição de defeitos"
        else:
            defeitos = self.quebrar_linhas(defeitos, 50)
        
        autor = input("Autor: ")
        idioma = input("Idioma: ")
        editora = input("Editora: ")
        data_publicacao = input("Data de publicação: ")
        qtd_paginas = input("Quantidade de páginas: ")
        dimensoes = input("Dimensões (L x A x P): ")
        isbn_10 = input("ISBN-10: ")
        isbn_13 = input("ISBN-13: ")
        edicao = input("Edição: ")
        volume = input("Volume: ")
        produto = Produto(id, nome, preco, quantidade, tipo_produto, descricao, eh_importado, estado, defeitos, autor, idioma, editora, data_publicacao, qtd_paginas, dimensoes, isbn_10, isbn_13, edicao, volume)
    
        self.bd_produtos.adicionar_produto(produto)
        print("Produto cadastrado com sucesso!")

    def listar_produtos(self): # função para listar produtos  
        produtos = self.bd_produtos.lista_produtos
        if len(produtos) > 0:
            for produto in produtos:
                print('='*50)
                print(f"Id: {produto.id_produto}")
                print(f"Nome: {produto.nome}")
                print(f"Preço: {produto.preco}")
                print(f"Quantidade: {produto.quantidade}")
                print(f"Tipo: {produto.tipo_produto}")
                print("="*60)
                print(f"Descrição do produto: {produto.descricao}")
                print("="*60)
                print(f"Importado: {produto.eh_importado}")
                print(f"Estado: {produto.estado}")
                print(f"Defeitos: {produto.defeitos}")
                print(f"Autor: {produto.autor}")
                print(f"Idioma: {produto.idioma}")
                print(f"Editora: {produto.editora}")
                print(f"Data de publicação: {produto.data_publicacao}")
                print(f"Quantidade de páginas: {produto.qtd_paginas}")
                print(f"ISBN-10: {produto.isbn_10}")
                print(f"ISBN-13: {produto.isbn_13}")
                print(f"Edição: {produto.edicao}")
                print(f"Volume: {produto.volume}")
                print('='*50, "\n")
        else:
            print("Não há produtos cadastrados!")
 


    def remover_produto(self): # função para remover produto
        id_produto = int(input("Id do produto: "))
        if self.bd_produtos.remover_produto(id_produto):
            print("Produto removido com sucesso!")
        else:
            print("Erro: produto não encontrado!")
    
    def alterar_produto(self): # função para atualizar produto
        id_produto = int(input("Id do produto: "))
        produto = self.bd_produtos.buscar_produto(id_produto)
        if produto != None:
            novo_nome = input("Novo nome: ")
            try:
                novo_preco = float(input("Novo preço: "))
                while novo_preco < 0:
                    print("Erro: Preço inválido!")
                    novo_preco = float(input("Novo preço: "))
            except ValueError:
                print("Erro: Preço inválido!")
                novo_preco = float(input("Novo preço: "))
            try:
                nova_quantidade = int(input("Nova quantidade: "))
                while nova_quantidade < 0:
                    print("Erro: Quantidade inválida!")
                    nova_quantidade = int(input("Nova quantidade: "))
            except ValueError:
                print("Erro: Quantidade inválida!")
                nova_quantidade = int(input("Nova quantidade: "))
            print("Tipo do produto: 1 - Livro | 2 - HQ | 3 - Manga | 4 - Box")
            try:
                opcao = int(input("Tipo do produto: "))
                while opcao < 1 or opcao > 4:
                    print("Erro: Opção inválida!")
                    opcao = int(input("Tipo do produto: "))
            except ValueError:
                print("Erro: Opção inválida!")
                opcao = int(input("Tipo do produto: "))
            if opcao == 1:
                novo_tipo_produto = "Livro"
            elif opcao == 2:
                novo_tipo_produto = "HQ"
            elif opcao == 3:
                novo_tipo_produto = "Manga"
            elif opcao == 4:
                novo_tipo_produto = "Box"
            novo_descricao = input("Descrição: ")
            novo_descricao = self.quebrar_linhas(novo_descricao, 50)
            try:
                novo_eh_importado = int(input("Importado: 1 - Sim | 2 - Não: "))
                while novo_eh_importado < 1 or novo_eh_importado > 2:
                    print("Erro: Opção inválida!")
                    novo_eh_importado = int(input("Importado: 1 - Sim | 2 - Não: "))
            except ValueError:
                print("Erro: Opção inválida!")
                novo_eh_importado = int(input("Importado: 1 - Sim | 2 - Não: "))
            if novo_eh_importado == 1:
                novo_eh_importado = True
            elif novo_eh_importado == 2:
                novo_eh_importado = False
            try:
                novo_estado = int(input("Estado: 1 - Novo | 2 - Usado: "))
                while novo_estado < 1 or novo_estado > 2:
                    print("Erro: Opção inválida!")
                    novo_estado = int(input("Estado: 1 - Novo | 2 - Usado: "))
            except ValueError:
                print("Erro: Opção inválida!")
                novo_estado = int(input("Estado: 1 - Novo | 2 - Usado: "))
            if novo_estado == 1:
                novo_estado = "Novo"
            elif novo_estado == 2:
                novo_estado = "Usado"
            novo_defeitos = input("Defeitos: ")
            novo_defeitos = self.quebrar_linhas(novo_defeitos, 50)
            novo_autor = input("Autor: ")
            novo_idioma = input("Idioma: ")
            novo_editora = input("Editora: ")
            novo_data_publicacao = input("Data de publicação: ")
            novo_qtd_paginas = input("Quantidade de páginas: ")
            novo_dimensoes = input("Dimensões (L x A x P): ")
            novo_isbn_10 = input("ISBN-10: ")
            novo_isbn_13 = input("ISBN-13: ")
            novo_edicao = input("Edição: ")
            novo_volume = input("Volume: ")
            #novo_produto = Produto(id_produto, novo_nome, novo_preco, nova_quantidade, novo_tipo_produto, novo_descricao, novo_eh_importado, novo_estado, novo_defeitos, novo_autor, novo_idioma, novo_editora, novo_data_publicacao, novo_qtd_paginas, novo_dimensoes, novo_isbn_10, novo_isbn_13, novo_edicao, novo_volume)
            self.bd_produtos.atualizar_produto(id_produto, novo_nome, novo_preco, nova_quantidade, novo_tipo_produto, novo_descricao, novo_eh_importado, novo_estado, novo_defeitos, novo_autor, novo_idioma, novo_editora, novo_data_publicacao, novo_qtd_paginas, novo_dimensoes, novo_isbn_10, novo_isbn_13, novo_edicao, novo_volume)
            
            if self.bd_produtos.atualizar_produto(id_produto, novo_nome, novo_preco, nova_quantidade, novo_tipo_produto, novo_descricao, novo_eh_importado, novo_estado, novo_defeitos, novo_autor, novo_idioma, novo_editora, novo_data_publicacao, novo_qtd_paginas, novo_dimensoes, novo_isbn_10, novo_isbn_13, novo_edicao, novo_volume):
                print("Produto atualizado com sucesso!")
            else:
                print("Erro: produto não encontrado!")
        else:
            print("Erro: produto não encontrado!")
    
    def buscar_produto(self): # função para buscar produto
        try:
            id_produto = int(input("Id do produto: "))
        except ValueError:
            print("Erro: Id inválido!")
            return
        produto = self.bd_produtos.buscar_produto(id_produto)
        if produto:
            print("Id: ", produto.id_produto)
            return produto

        else:
            print("Erro: produto não encontrado!")


            






  




            

            



    

