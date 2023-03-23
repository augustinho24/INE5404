from ingresso import Ingresso
from ingresso import VIP
from ingresso import Normal
from ingresso import CamaroteInferior
from ingresso import CamaroteSuperior

lista_ingressos = []

valor_ingresso = 1.99
adicional_vip_ingresso = 60.99
adicional_camarote_ingresso = 40



def menu():
    print('/' *15,"Menu",'/' *15)
    print()
    print("0 - Sair")
    print("1 - Cadastrar Ingresso")
    print("2 - Listar Ingressos")
    print("3 - Alterar cadastro de um Ingresso")

    opcao = int(input("Digite a opção desejada: "))
    return opcao

def cadastrar_ingresso():
    nome = input("Digite o nome: ")
    print( "1 - Normal", end="\n" "2 - VIP")
    opcao_tipo = int(input())
    if opcao_tipo == 1:
        tipo = "Normal"
        lista_ingressos.append(Normal(nome,valor,tipo))
    elif opcao_tipo == 2:
        tipo = "VIP"
        valor = valor + adicional_vip_ingresso
    else:
        opcao_tipo = int(input("Insira novamente: "))

    if tipo == "VIP":
        print("1 - Camarote Inferior", end="\n" "2 - Camarote Superior")
        opcao_camarote = int(input())
        if opcao_camarote == 1: 
            camarote = "Camarote Inferior"
            lista_ingressos.append(CamaroteInferior(nome,valor,tipo,adicional_vip_ingresso,camarote))
        elif opcao_camarote == 2:
            camarote = "Camarote Superior"
            valor = valor_ingresso + adicional_vip_ingresso + adicional_camarote_ingresso
            lista_ingressos.append(CamaroteSuperior(nome,valor,tipo,adicional_vip_ingresso,camarote,adicional_camarote_ingresso))
        else:
            opcao_camarote = int(input("Insira novamente: "))



    
aa = "ADOADO"
aa.upper()

adoado



    
































while True:
    opcao = menu()
    if opcao == 1:
        
    elif opcao == 2:
  
    elif opcao == 3:
        
    
    elif opcao == 0:
        break
    else:
        print("Opção inválida")