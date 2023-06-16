class Estoque: # Classe que armazena os carros
    def __init__(self):
        self.lista_carros = [] # lista de carros
        self.set_ids_carros = set() # conjunto de ids de carros, para evitar repetição

    def buscar_carro(self, id): # busca o carro pelo id
        for carro in self.lista_carros:
            if carro.id == id:
                return carro
        return None
    
    def verifica_id(self, id): # verifica se o id já existe no conjunto
        if id in self.set_ids_carros:
            return True
        return False

    def adicionar_carro(self, carro): # adiciona o carro na lista e no conjunto
        self.lista_carros.append(carro)
        self.set_ids_carros.add(carro.id)
        print("Carro adicionado com sucesso.")
        return True 
    
    def remover_carro(self, carro): # remove o carro e seu id da lista e do conjunto
        self.lista_carros.remove(carro)
        self.set_ids_carros.remove(carro.id)
        print("Carro removido com sucesso.")
        return True

    def atualizar_carro(self, id, novo_marca, novo_modelo, novo_ano_abricacao, novo_preco, novo_estado):
        carro = self.buscar_carro(id)
        if carro:
            carro.marca = novo_marca
            carro.modelo = novo_modelo
            carro.ano_fabricacao = novo_ano_abricacao
            carro.preco = novo_preco
            carro.estado = novo_estado
            print("Carro atualizado com sucesso.")
            return True
        print("Erro: carro não encontrado.")
        return False


