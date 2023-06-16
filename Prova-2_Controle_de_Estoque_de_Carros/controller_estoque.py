from carro import Carro
from estoque import Estoque

class ControllerEstoque: # Classe que interage com o usuário e com a classe Estoque
    def __init__(self):
        self.estoque = Estoque()

    def cadastrar_carro(self, id, marca, modelo, ano_fabricacao, preco, estado):
        try:
            if self.estoque.verifica_id(id):
                print("Erro: id já existente.")
            else:
                carro = Carro(id, marca, modelo, ano_fabricacao, preco, estado)
                self.estoque.adicionar_carro(carro)
        except ValueError:
            print("Erro: id inválido.")

                
    def atualizar_carro(self, id, novo_marca, novo_modelo, novo_ano_fabricacao, novo_preco, novo_estado):
        try:
            if self.estoque.verifica_id(id):
                self.estoque.atualizar_carro(id, novo_marca, novo_modelo, novo_ano_fabricacao, novo_preco, novo_estado)
            else:
               print("Erro: id não encontrado.")
        except ValueError:
            print("Erro: id inválido.")
        
    def listar_carros(self):
#        carros = self.estoque.lista_carros
#        if carros:
#            for carro in carros:
#                self.exibir_carro(carro)
#        else:
#            print("Nenhum carro cadastrado.")
#
#    def exibir_carro(self, carro):
#        print("="*20)
#        print(f"ID: {carro.id}\n"
#            f"Marca: {carro.marca}\n"
#            f"Modelo: {carro.modelo}\n"
#            f"Ano: {carro.ano_fabricacao}\n"
#            f"Preço: {carro.preco}\n"
#            f"Estado: {carro.estado}")
#        print("="*20, "\n")
        carros = self.estoque.lista_carros
        return carros


    def listar_carros_por_marca(self, marca):      
        carros_encontrados = [carro for carro in self.estoque.lista_carros if carro.marca == marca]
        #if carros_encontrados:
        #    for carro in carros_encontrados:
        #        print("="*20)
        #        print(f"ID: {carro.id}\n"
        #            f"Marca: {carro.marca}\n"
        #            f"Modelo: {carro.modelo}\n"
        #            f"Ano: {carro.ano_fabricacao}\n"
        #            f"Preço: {carro.preco}\n"
        #            f"Estado: {carro.estado}")
        #        print("="*20,"\n")
        if not carros_encontrados:
            print("Nenhum carro encontrado.")
        return carros_encontrados


    def remover_carro(self, id):
        try:
            id = int(id)
            if self.estoque.verifica_id(id):
                carro = self.estoque.buscar_carro(id)
                self.estoque.remover_carro(carro)
            else:
                print("Erro: ID não encontrado.")
        except ValueError:
            print("Erro: ID inválido.")
        except AttributeError:
            print("Erro: Atributo inválido.")
  

    def calcular_media_precos(self):
        soma = 0
        for carro in self.estoque.lista_carros:
            soma += carro.preco
        while True:
            try:
                media = soma / len(self.estoque.lista_carros)
                break
            except ZeroDivisionError:
                print("Erro: nenhum carro cadastrado.")
                return
        return media
    



        
    


        

    