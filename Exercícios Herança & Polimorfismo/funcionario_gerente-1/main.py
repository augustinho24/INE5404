from funcionario import Funcionario
from funcionario import Assistente
from funcionario import Assistente_Tecnico
from gerente import Gerente



lista_funcionarios = []
lista_gerentes = []

def menu():
    print('/' *15,"Menu",'/' *15)
    print()
    print("0 - Sair")
    print("1 - Cadastrar Funcionário")
    print("2 - Cadastrar Gerente")
    print("3 - Listar Funcionários")
    print("4 - Listar Gerentes")
    print("5 - Alterar cadastro de um funcionário")

    opcao = int(input("Digite a opção desejada: "))
    return opcao

def cadastrar_funcionario():
    num_matricula = int(input("Digite o número de matrícula: "))
    cpf = int(input("Digite o CPF: "))
    nome = input("Digite o nome: ").capitalize()
    sexo = input("Digite o sexo: ").upper()
    while sexo != "M" and sexo != "F":
        print("Inválido")
        sexo = input("Digite o sexo: ").upper()
    idade = int(input("Digite a idade: "))
    salario = float(input("Digite o salário: "))
    cargo = int("Digite o cargo: ")
    turno = input("Digite o turno: ").lower()
    if cargo == "Assistente Técnico" and turno == "noturno":
        adicional = float(input("Digite o adicional: "))
    else:
        adicional = 0
    if cargo == "Assistente":
        lista_funcionarios.append(Assistente(num_matricula, cpf, nome, sexo, idade, salario, cargo, turno, adicional))
    elif cargo == "Assistente Técnico":
        lista_funcionarios.append(Assistente_Tecnico(num_matricula, cpf, nome, sexo, idade, salario, cargo, turno, adicional))
    else:
        lista_funcionarios.append(Funcionario(num_matricula, cpf, nome, sexo, idade, salario, cargo, turno, adicional))
    
def cadastrar_gerente():
    num_matricula = int(input("Digite o número de matrícula: "))
    cpf = int(input("Digite o CPF: "))
    nome = input("Digite o nome: ")
    sexo = input("Digite o sexo: ")
    idade = int(input("Digite a idade: "))
    salario = float(input("Digite o salário: "))
    cargo = input("Digite o cargo: ")
    turno = input("Digite o turno: ").lower()
    adicional = 0
    lista_gerentes.append(Gerente(num_matricula, cpf, nome, sexo, idade, salario, cargo, turno, adicional))

def alterar_cadastro():
    num_matricula = int(input("Digite o número de matrícula: "))
    for f in lista_funcionarios:
        if f.get_num_matricula() == num_matricula:
            print("1 - Alterar nome")
            print("2 - Alterar idade")
            print("3 - Alterar salário")
            print("4 - Alterar cargo")
            print("5 - Alterar turno")
            print("6 - Alterar adicional")
            print("0 - Sair")
            opcao = int(input("Digite a opção desejada: "))
            while opcao != 0:
                if opcao == 1:
                    novo_nome = input("Digite o novo nome: ")
                    f.set_nome(novo_nome)
                elif opcao == 2:
                    nova_idade = int(input("Digite a nova idade: "))
                    f.set_idade(nova_idade)
                elif opcao == 3:
                    novo_salario = float(input("Digite o novo salário: "))
                    f.set_salario(novo_salario)
                elif opcao == 4:
                    novo_cargo = input("Digite o novo cargo: ")
                    f.set_cargo(novo_cargo)
                elif opcao == 5:
                    novo_turno = input("Digite o novo turno: ")
                    f.set_turno(novo_turno)
                elif novo_cargo == "Assistente Técnico" and opcao == 6:
                    novo_adicional = float(input("Digite o novo adicional: "))
                    f.set_adicional(novo_adicional)
        else:
            print("Funcionário não encontrado")

def listar_gerentes():
    for g in lista_gerentes:
        print("/" * 50)
        print("Número de matrícula: ", g.get_num_matricula())
        print("CPF: ", g.get_cpf())
        print("Nome: ", g.get_nome())
        print("Sexo: ", g.get_sexo())
        print("Idade: ", g.get_idade())
        print("Salário: ", g.get_salario())
        print("Cargo: ", g.get_cargo())
        print("Turno: ", g.get_turno())
        print("Adicional: ", g.get_adicional())
        print("")




def listar_funcionarios():
    for f in lista_funcionarios:
        print("/" * 50)
        print("Número de matrícula: ", f.get_num_matricula())
        print("CPF: ", f.get_cpf())
        print("Nome: ", f.get_nome())
        print("Sexo: ", f.get_sexo())
        print("Idade: ", f.get_idade())
        print("Salário: ", f.get_salario())
        print("Cargo: ", f.get_cargo())
        print("Turno: ", f.get_turno())
        print("Adicional: ", f.get_adicional())
        print("")

while True:
    opcao = menu()
    if opcao == 1:
        cadastrar_funcionario()
    elif opcao == 2:
        cadastrar_gerente()
    elif opcao == 3:
        listar_funcionarios()
    elif opcao == 4:
        listar_gerentes()
    elif opcao == 5:
        alterar_cadastro()
    elif opcao == 0:
        break
    else:
        print("Opção inválida")



    
