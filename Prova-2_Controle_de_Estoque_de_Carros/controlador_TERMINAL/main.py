from controller_estoque import ControllerEstoque

class ViewEstoque:
    def __init__(self):
        self.controller_estoque = ControllerEstoque()
    
    def menu(self):
        print("Controle de Estoque da Loja de Carros\n1 - Cadastrar carro\n"
            "2 - Atualizar carro\n"
            "3 - Remover carro\n"
            "4 - Listar carros\n"
            "5 - Listar carros por marca\n"
            "6 - Calcular a média dos preços dos carros\n"
            "0 - Sair\n")
        while True:
            try:
                opcao = int(input("Digite a opção desejada: "))
                break
            except ValueError:
                print("Erro: opção inválida.")
        while opcao < 0 or opcao > 9:
            print("Erro: opção inválida.")
            opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            self.controller_estoque.cadastrar_carro()
        elif opcao == 2:
            self.controller_estoque.atualizar_carro()
        elif opcao == 3:
            self.controller_estoque.remover_carro()
        elif opcao == 4:
            self.controller_estoque.listar_carros()
        elif opcao == 5:
            self.controller_estoque.listar_carros_por_marca(marca= input("Digite a marca: "))
        elif opcao == 6:
            self.controller_estoque.calcular_media_precos()
        elif opcao == 0:
            print("Saindo...")
            exit()
        self.menu()

    
if __name__ == "__main__":
    view_estoque = ViewEstoque()
    view_estoque.menu()

    