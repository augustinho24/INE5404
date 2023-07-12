class BD_Pessoas:
    def __init__(self):
        self.lista_clientes = [] # lista de clientes
        #self.lista_funcionarios = [] # lista de funcionários
        self.conjunto_id_pessoas = set() # conjunto de ids de pessoas cadastradas
        self.conjunto_usuario = set() # conjunto de usuários cadastrados
        self.conjunto_senha = set() # conjunto de senhas cadastradas
        self.conjunto_id_compras = set() # conjunto de ids de compras realizadas
        self.lista_compras = [] # lista de compras realizadas

    
    def buscar_cliente(self, id): # busca cliente pelo id
        for cliente in self.lista_clientes:
            if cliente.id_pessoa == id:
                return cliente
        return None
    
    def verifica_id(self, id): # verifica se o id já está cadastrado
        if id in self.conjunto_id_pessoas:
            return True
        else:
            return False
        
    def verifica_usuario(self, usuario): # verifica se o usuário já está cadastrado
        if usuario in self.conjunto_usuario:
            return True
        else:
            return False
    
    def verifica_senha(self, senha): # verifica se a senha já está cadastrada
        if senha in self.conjunto_senha:
            return True
        else:
            return False
    
    def verifica_id_compra(self, id): # verifica se o id da compra já está cadastrado
        if id in self.conjunto_id_compras:
            return True
        else:
            return False
    
    def adicionar_cliente(self, cliente): # adiciona cliente
        self.lista_clientes.append(cliente)
        self.conjunto_id_pessoas.add(cliente.id_pessoa)
        self.conjunto_usuario.add(cliente.usuario)
        self.conjunto_senha.add(cliente.senha)
        self.lista_clientes.sort(key=lambda x: x.id_pessoa) # ordenar a lista por ordem crescente pelo id
        #print("Cliente adicionado com sucesso!")

    def remover_cliente(self, cliente): # remove cliente
        self.lista_clientes.remove(cliente)
        self.conjunto_id_pessoas.remove(cliente.id_pessoa)
        self.conjunto_usuario.remove(cliente.usuario)
        self.conjunto_senha.remove(cliente.senha)
        self.lista_clientes.sort(key=lambda x: x.id_pessoa)
        print("Cliente removido com sucesso!")
    
    def atualizar_cliente(self, id, novo_nome, novo_idade, novo_cpf, novo_email, novo_usuario, novo_senha): # atualiza cliente
        cliente = self.buscar_cliente(id)
        if cliente:
            cliente.nome = novo_nome
            cliente.idade = novo_idade
            cliente.cpf = novo_cpf
            cliente.email = novo_email
            cliente.usuario = novo_usuario
            cliente.senha = novo_senha
            print("Cliente atualizado com sucesso!")
            return True
        print("Erro: cliente não encontrado!")
        return False
    
    def add_compra_lista(self, compra):
        self.lista_compras.append(compra)
        self.lista_compras.sort(key=lambda x: x.id_compra)
        print("Compra registrada com sucesso!")


    
        




    



    
