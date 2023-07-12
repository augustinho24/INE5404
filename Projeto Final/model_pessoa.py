class Pessoa:
    def __init__(self, id_pessoa, tipo_cadastro, nome, idade, cpf, email, usuario, senha):
        self.id_pessoa = id_pessoa
        self.tipo_cadastro = tipo_cadastro
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.usuario = usuario
        self.senha = senha

class Cliente(Pessoa):
    def __init__(self, id_pessoa, tipo_cadastro, nome, idade, cpf, email, usuario, senha, historico_compras, carrinho):
        super().__init__(id_pessoa, tipo_cadastro, nome, idade, cpf, email, usuario, senha)
        self.historico_compras = historico_compras
        self.carrinho = carrinho # dicionário contendo produto e suas respectivas quantidades

    

    def add_compra_historico(self, compra):
        self.historico_compras.append(compra)


    def add_produto_carrinho(self, produto, quantidade): # adiciona produto ao carrinho
        self.carrinho[produto] = quantidade

    def remover_produto_carrinho(self, produto): # remove produto do carrinho
        if produto in self.carrinho:
            del self.carrinho[produto]
            return True
        return False

    def listar_carrinho(self): # exibe produtos do carrinho
        if len(self.carrinho) == 0:
            print("Carrinho vazio!")
            return
        print("#" * 50, "Produtos no Carrinho", "#" * 50, "\n")
        for produto, quantidade in self.carrinho.items():
            print(f"ID: {produto.id_produto} | Nome: {produto.nome} | Preco p/Unidade: {produto.preco} - Quantidade: {quantidade}\n")
        return
    
    def listar_historico_compras(self):
        if len(self.historico_compras) == 0:
            print("Histórico de compras vazio!")
            return
        print("#" * 50, "Histórico de Compras", "#" * 50, "\n")
        for compra in self.historico_compras:
            produtos = compra.produtos # dicionário contendo produto e suas respectivas quantidades
            print(f"ID: {compra.id_compra} | Data: {compra.data_compra} | Valor: {compra.valor_total}\n")
            print("#" * 30, "Produtos", "#" * 30, "\n")
            for produto, quantidade in produtos.items():
                print(f"ID: {produto.id_produto} | Nome: {produto.nome} | Preco p/Unidade: {produto.preco} - Quantidade: {quantidade}\n")
       
        return

