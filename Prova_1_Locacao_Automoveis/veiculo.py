from locadora_carros import Locadora_de_carros

locadora_inst = Locadora_de_carros()

class Veiculo():
    def __init__(self, id_veiculo = '', modelo = '', ano=0, placa='', valor_diaria='', disponivel=True):
        self.id_veiculo = id_veiculo
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.valor_diaria = valor_diaria
        self.disponivel = True

def get_id_veiculo(self):
    return self.id_veiculo
def set_id_veiculo(self, id_veiculo):
    self.id_veiculo = id_veiculo

def get_modelo(self):
    return self.modelo
def set_modelo(self, modelo):
    self.modelo = modelo

def get_ano(self):
    return self.ano
def set_ano(self, ano):
    self.ano = ano
def get_placa(self):
    return self.placa
def set_placa(self, placa):
    self.placa = placa

def get_valor_diaria(self):
    return self.valor_diaria
def set_valor_diaria(self, valor_diaria):
    self.valor_diaria = valor_diaria

def get_disponivel(self):
    return self.disponivel
def set_disponivel(self, disponivel):
    self.disponivel = disponivel

def cadastrar_veiculo():
    id_veiculo = int(input('ID: '))
    modelo = input('Modelo: ')
    ano = int(input('Ano: '))
    placa = input('Placa: ')
    valor_diaria = float(input('Valor da diária: '))
    veiculo = Veiculo(id_veiculo, modelo, ano, placa, valor_diaria, True)
    locadora_inst.set_veiculos_disponiveis(veiculo)
    print('Veículo cadastrado com sucesso!')
    
def alterar_cadastro_veiculo():
    id_veiculo = int(input('ID do veículo: '))
    for veiculo in locadora_inst.get_veiculos_disponiveis():
        if veiculo.get_id_veiculo() == id_veiculo:
            print('O que deseja alterar?')
            print('1 - Modelo')
            print('2 - Ano')
            print('3 - Placa')
            print('4 - Valor da diária')
            print('5 - Disponível')
            print('0 - Sair\n')
            opcao = int(input('Opção: '))
            while opcao != 0:
                while opcao < 1 or opcao > 5:
                    print('Opção inválida!')
                    opcao = int(input('Digite a opção novamente: '))
                if opcao == 1:
                    modelo = input('Modelo: ')
                    veiculo.set_modelo(modelo)
                elif opcao == 2:
                    ano = int(input('Ano: '))
                    veiculo.set_ano(ano)
                elif opcao == 3:
                    placa = input('Placa: ')
                    veiculo.set_placa(placa)
                elif opcao == 4:
                    valor_diaria = float(input('Valor da diária: '))
                    veiculo.set_valor_diaria(valor_diaria)
                print('Cadastro alterado com sucesso!')
                break
        else:
            print('Veículo não encontrado!')
    
def excluir_veiculo():
    id_veiculo = int(input('ID do veículo: '))
    for veiculo in locadora_inst.get_veiculos_disponiveis():
        if veiculo.get_id_veiculo() == id_veiculo:
            locadora_inst.get_veiculos_disponiveis().remove(veiculo)
            print('Veículo excluído com sucesso!')
            break
    else:
        print('Veículo não encontrado!')

def listar_veiculos():
    print('Veículos cadastrados:')
    for veiculo in locadora_inst.get_veiculos_disponiveis():
        print(f'ID: {veiculo.get_id()}')
        print(f'Nome: {veiculo.get_nome()}')
        print(f'Placa: {veiculo.get_placa()}')
        print(f'Ano: {veiculo.get_ano()}')
        print(f'Valor da diária: R$ {veiculo.get_valor_diaria()}')
        print(f'Disponível: {veiculo.get_disponivel()}')
        print('------------------------------------')










