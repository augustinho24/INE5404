from carro import Carro
from estoque import Estoque

class ControllerEstoque: # Classe que interage com o usuário e com a classe Estoque
    def __init__(self):
        self.estoque = Estoque()

### ADAPTAR AS FUNÇÕES PARA INTERFACE GRÁFICA USANDO TKINTER ###

    def cadastrar_carro(self): ###
        if self.estoque.verifica_id(id):
            print("Erro: id já existente.")
        else:
            carro = Carro(id, marca, modelo, ano_fabricacao, preco, estado)
            self.estoque.adicionar_carro(carro)

    def atualizar_carro(self):
        try:
            if self.estoque.verifica_id(id):
                self.estoque.atualizar_carro(id, novo_marca, novo_modelo, novo_ano_fabricacao, novo_preco, novo_estado)
            else:
                print("Erro: id não encontrado.")
        except ValueError:
            print("Erro: id inválido.")

    def listar_carros(self):
        if self.estoque.lista_carros:
            for carro in self.estoque.lista_carros:
                print("="*20)
                print(f"ID: {carro.id}\n"
                    f"Marca: {carro.marca}\n"
                    f"Modelo: {carro.modelo}\n"
                    f"Ano: {carro.ano_fabricacao}\n"
                    f"Preço: {carro.preco}\n"
                    f"Estado: {carro.estado}")
                print("="*20,"\n")
        else:
            print("Nenhum carro cadastrado.")

    def listar_carros_por_marca(self, marca):      
        carros_encontrados = [carro for carro in self.estoque.lista_carros if carro.marca == marca]
        if carros_encontrados:
            for carro in carros_encontrados:
                print("="*20)
                print(f"ID: {carro.id}\n"
                    f"Marca: {carro.marca}\n"
                    f"Modelo: {carro.modelo}\n"
                    f"Ano: {carro.ano_fabricacao}\n"
                    f"Preço: {carro.preco}\n"
                    f"Estado: {carro.estado}")
                print("="*20,"\n")
        else:
            print(f"Nenhum carro da marca '{marca}' encontrado.")



    def remover_carro(self):
        id = int(input("Digite o id do carro: "))
        try:
            id = int(id)
        except ValueError:
            print("Erro: id inválido.")
            id = int(input("Digite o id do carro: "))
        if not self.estoque.verifica_id(id):
            print("Erro: id não encontrado.")
            #voltar ao menu
        self.estoque.remover_carro(id)

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
        print(f"A média de preços dos carros é: {media:.2f}")
    



        
    


        

    