from locadora_carros import Locadora_de_carros
from pessoa import Pessoa
from veiculo import Veiculo
from pessoa import cadastro_Pessoa, login

locadora_inst = Locadora_de_carros()
pessoa_inst = Pessoa()
veiculo_inst = Veiculo()



def menu_inicial():
    #importar o nome da locadora
    print("Bem vindo a Fogaréu Rent Não-Me-Toque")
    print('//' *15, "Menu", '//' *15)
    print("1 -  Criar cadastro")
    print("2 -  Login")
    print("0 -  Sair")
    print('//' *20, '//' *20)

while True:
    menu_inicial()
    opcao = int(input('Opção: '))
    if opcao == 1:
        cadastro_Pessoa()
    elif opcao == 2:
       login()

    elif opcao == 0:
        break
    else:
        print('Opção inválida!\n')
        continue


    
