from carro import Carro
from estoque import Estoque

class ControllerEstoque: # Classe que interage com o usuário e com a classe Estoque
    def __init__(self):
        self.estoque = Estoque()

    def cadastrar_carro(self):
        while True:
            try:
                id = int(input("Digite um id para o carro: "))
                if self.estoque.verifica_id(id):
                    print("Erro: id já existente.")
                else:
                    break
            except ValueError:
                print("Erro: id inválido.")

        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")

        while True:
            try:
                ano_fabricacao = int(input("Digite o ano de fabricação do carro: "))
                break
            except ValueError:
                print("Erro: ano de fabricação inválido.")

        while True:
            try:
                preco = float(input("Digite o preço do carro: "))
                break
            except ValueError:
                print("Erro: preço inválido.")

        while True:
            try:
                opcao = int(input("1 - Novo\n2 - Usado\nDigite a opção desejada: "))
                if opcao < 1 or opcao > 2:
                    print("Erro: opção inválida.")
                else:
                    break
            except ValueError:
                print("Erro: opção inválida.")

        if opcao == 1:
            estado = "Novo"
        elif opcao == 2:
            estado = "Usado"

        carro = Carro(id, marca, modelo, ano_fabricacao, preco, estado)
        self.estoque.adicionar_carro(carro)

    def atualizar_carro(self):
        while True:
            try:
                id = int(input("Digite o id do carro: "))
                if self.estoque.verifica_id(id):
                    break
                else:
                    print("Erro: id não encontrado.")
                    return
            except ValueError:
                print("Erro: id inválido.")

        novo_marca = input("Digite a nova marca do carro: ")
        novo_modelo = input("Digite o novo modelo do carro: ")

        while True:
            try:
                novo_ano_fabricacao = int(input("Digite o novo ano de fabricação do carro: "))
                break
            except ValueError:
                print("Erro: ano de fabricação inválido.")

        while True:
            try:
                novo_preco = float(input("Digite o novo preço do carro: "))
                break
            except ValueError:
                print("Erro: preço inválido.")

        while True:
            try:
                opcao = int(input("1 - Novo\n2 - Usado\nDigite a opção desejada: "))
                if opcao < 1 or opcao > 2:
                    print("Erro: opção inválida.")
                else:
                    break
            except ValueError:
                print("Erro: opção inválida.")

        if opcao == 1:
            novo_estado = "Novo"
        elif opcao == 2:
            novo_estado = "Usado"

        self.estoque.atualizar_carro(id, novo_marca, novo_modelo, novo_ano_fabricacao, novo_preco, novo_estado)
        
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
    



        
    


        

    