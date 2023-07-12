from model_pessoa import Cliente
from data_pessoas import BD_Pessoas
from data_produtos import BD_Produtos

class Controller_BD_pessoas:
    def __init__(self):
        self.bd_pessoas = BD_Pessoas()
        self.bd_produtos = BD_Produtos()

    def cadastrar_cliente(self):
        try:
            id = int(input("Id do cliente: "))
            while self.bd_pessoas.verifica_id(id):
                print("Erro: Id já cadastrado!")
                id = int(input("Id do cliente: "))
        except ValueError:
            print("Erro: Id inválido!")
            return
        nome = input("Nome do cliente: ")
        idade = input("Idade do cliente: ")
        cpf = input("CPF do cliente: ")
        email = input("Email do cliente: ")
        usuario = input("Usuário do cliente: ")
        while self.bd_pessoas.verifica_usuario(usuario):
            print("Erro: Usuário já cadastrado!")
            usuario = input("Usuário do cliente: ")
        senha = input("Senha do cliente: ")
        while self.bd_pessoas.verifica_senha(senha):
            print("Erro: Senha já cadastrada!")
            senha = input("Senha do cliente: ")
        historico_compras = []
        carrinho = {}
        cliente = Cliente(id, "Cliente", nome, idade, cpf, email, usuario, senha, historico_compras, carrinho)
        self.bd_pessoas.adicionar_cliente(cliente)
        print("Cliente cadastrado com sucesso!")

    def alterar_cliente(self):
        try:
            id = int(input("Id do cliente: "))
            while not self.bd_pessoas.verifica_id(id):
                print("Erro: Id não cadastrado!")
                id = int(input("Id do cliente: "))
        except ValueError:
            print("Erro: Id inválido!")
            return
        nome = input("Nome do cliente: ")
        idade = input("Idade do cliente: ")
        cpf = input("CPF do cliente: ")
        email = input("Email do cliente: ")
        usuario = input("Usuário do cliente: ")
        while self.bd_pessoas.verifica_usuario(usuario):
            print("Erro: Usuário já cadastrado!")
            usuario = input("Usuário do cliente: ")
        senha = input("Senha do cliente: ")
        while self.bd_pessoas.verifica_senha(senha):
            print("Erro: Senha já cadastrada!")
            senha = input("Senha do cliente: ")
        self.bd_pessoas.atualizar_cliente(id, nome, idade, cpf, email, usuario, senha)
        print("Cliente atualizado com sucesso!")

    def remover_cliente(self):
        try:
            id = int(input("Id do cliente: "))
            while not self.bd_pessoas.verifica_id(id):
                print("Erro: Id não cadastrado!")
                id = int(input("Id do cliente: "))
        except ValueError:
            print("Erro: Id inválido!")
            return
        self.bd_pessoas.remover_cliente(id)
        print("Cliente removido com sucesso!")
    
    def pega_lista_clientes(self):
        return self.bd_pessoas.lista_clientes
    
    def listar_clientes(self):
        clientes = self.bd_pessoas.lista_clientes
        if len(clientes) == 0:
            print("Não há clientes cadastrados!")
            return
        for cliente in clientes:
            print("Id: ", cliente.id_pessoa)
            print("Nome: ", cliente.nome)
            print("Idade: ", cliente.idade)
            print("CPF: ", cliente.cpf)
            print("Email: ", cliente.email)
            print("Usuário: ", cliente.usuario)
            print("Senha: ", cliente.senha)
            print("Histórico de compras: ", cliente.historico_compras)
            print("Carrinho: ", cliente.carrinho)
            print("")

    

        


    



        
        

        
        


    

    


    
    





    

        

  
     
    

