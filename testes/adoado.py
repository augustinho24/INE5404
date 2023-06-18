class Carro:
    def __init__(self, id, marca, modelo, ano_fabricacao, preco, estado):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.preco = preco
        self.estado = estado


class Estoque:
    def __init__(self):
        self.lista_carros = []  # lista de carros
        self.set_ids_carros = set()  # conjunto de ids de carros, para evitar repetição

class EstoqueController:
    def __init__(self):
        self.estoque = Estoque()

    def adicionar_carro(self, id, marca, modelo, ano_fabricacao, preco, estado):
        if id in self.estoque.set_ids_carros:
            print("Carro com ID já existente.")
        else:
            carro = Carro(id, marca, modelo, ano_fabricacao, preco, estado)
            self.estoque.lista_carros.append(carro)
            self.estoque.set_ids_carros.add(id)
            print("Carro adicionado com sucesso.")

    def buscar_carro(self, id):
        for carro in self.estoque.lista_carros:
            if carro.id == id:
                print(f"ID: {carro.id}, Marca: {carro.marca}, Modelo: {carro.modelo}, Ano: {carro.ano_fabricacao}, "
                      f"Preço: {carro.preco}, Estado: {carro.estado}")
                break
        else:
            print("Carro não encontrado.")

    def atualizar_carro(self, id, marca, modelo, ano_fabricacao, preco, estado):
        for carro in self.estoque.lista_carros:
            if carro.id == id:
                carro.marca = marca
                carro.modelo = modelo
                carro.ano_fabricacao = ano_fabricacao
                carro.preco = preco
                carro.estado = estado
                print("Carro atualizado com sucesso.")
                break
        else:
            print("Carro não encontrado.")

    def excluir_carro(self, id):
        for i, carro in enumerate(self.estoque.lista_carros):
            if carro.id == id:
                del self.estoque.lista_carros[i]
                self.estoque.set_ids_carros.remove(id)
                print("Carro excluído com sucesso.")
                break
        else:
            print("Carro não encontrado.")

    def listar_carros(self):
        if self.estoque.lista_carros:
            print("==================")
            for carro in self.estoque.lista_carros:
                print(f"ID: {carro.id}\n"
                      f"Marca: {carro.marca}\n"
                      f"Modelo: {carro.modelo}\n"
                      f"Ano: {carro.ano_fabricacao}\n"
                      f"Preço: {carro.preco}\n"
                      f"Estado: {carro.estado}\n"
                      "==================")
        else:
            print("Nenhum carro encontrado.")


estoque_controller = EstoqueController()

# Adicionando carros
estoque_controller.adicionar_carro(1, "Marca 1", "Modelo 1", 2021, 50000, "Novo")
estoque_controller.adicionar_carro(2, "Marca 2", "Modelo 2", 2022, 60000, "Usado")
estoque_controller.adicionar_carro(3, "Marca 3", "Modelo 3", 2020, 40000, "Novo")

# Listando carros
estoque_controller.listar_carros()

# Buscando um carro
estoque_controller.buscar_carro(2)

# Atualizando um carro
estoque_controller.atualizar_carro(3, "Nova Marca", "Novo Modelo", 2023, 70000, "Usado")

# Listando carros novamente
estoque_controller.listar_carros()

# Excluindo um carro
estoque_controller.excluir_carro(1)

# Listando carros após exclusão
estoque_controller.listar_carros()