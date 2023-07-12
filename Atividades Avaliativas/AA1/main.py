
from funcionario import Funcionario
from funcionario import Vendedor
from funcionario import Administrativo
from funcionario import Gerente
from funcionario import AuxLimpeza
from cliente import Cliente
from produto import Produto
from produto import Compra
import re

listaFuncionarios = []
listaClientes = []
listaProdutos = []

def Menu():
    print('//' *15, 'Loja de Roupas dos Subconjuntos do Conjunto ∅', '//' *15)
    print()
    print('//' *15, "Menu", '//' *15)
    print("1 - Cadastrar Cliente")
    print("2 - Listar Cliente")
    print("3 - Alterar Cadastro do Cliente")
    print("4 - Cadastrar Funcionário")
    print("5 - Listar Funcionário")
    print("6 - Alterar Cadastro do Funcionário")
    print("7 - Cadastrar Produto")
    print("8 - Listar Produto")
    print("9 - Alterar Cadastro do Produto")
    print("10 - Login Cliente")
    print("11 - Remover cadastro do Cliente") 
    print("12 - Remover cadastro do Funcionário")
    print("13 - Remover cadastro do Produto")
    print("0 - Sair")
    print('//' *20, '//' *20)

    opcao = int(input("Digite a opção desejada:"))
    return opcao


def verifica_string(string):
    if re.search('[a-zA-Z]', string) and re.search('[0-9]', string):
        return True
    else:
        return False

def cadastrarCliente():
    nome = input("Digite o nome: ")
    rg = int(input("Digite o rg: "))
    endereco = input("Digite o endereco: ")
    telefone = int(input("Digite o telefone: "))
    email = input("Digite o endereço eletrônico: ")
    senha = input("Digite a senha (obrigatório conter letras e números): ")
    while verifica_string(senha) == False:
        print("Senha inválida!")
        senha = input("Digite a senha (obrigatório conter letras e números): ")
    historico_compras = []
    listaClientes.append(Cliente(nome, rg, endereco, telefone, email, senha, historico_compras))


def consultar_historico_compras(email, senha):
    for j in listaClientes:
        if email == j.getEmail() and senha == j.getSenha():
            historico_compras = j.getHistoricoCompras()
    for i in historico_compras:
        print('Departamento: ', i.getDepartamento())
        print("Tipo: ", i.getTipo())
        print("Tamanho: ", i.getTamanho())
        print("Genero: ", i.getGenero())
        print("Quantidade: ", i.getUnidades())
        print("Total: ", i.getTotal())
        print("Forma de pagamento: ", i.getFormaPagamento())
        print("Desconto: ", i.getDesconto())
        print("")


def login_cliente():
    email = input("Digite o email: ")
    senha = input("Digite a senha: ")
    for i in listaClientes:
        if email == i.getEmail() and senha == i.getSenha():
            while True:
                print("")
                print("Bem vindo(a) ", i.getNome())
                print("1 - Comprar")
                print("2 - Consultar histórico de compras")
                print("3 - Consultar produtos")
                print("0 - Sair")
                opcao = int(input("Digite a opção desejada:"))
                if opcao == 1:
                    codigo_serial = input("Digite o código serial do produto: ")
                    for u in listaProdutos:
                        if codigo_serial == u.getCodigoSerial():
                            unidades = int(input("Digite a quantidade de unidades: "))
                            for j in listaProdutos:
                                if codigo_serial == j.getCodigoSerial():
                                    if unidades > j.getUnidades():
                                        print("Quantidade indisponível!")
                                    else:
                                        j.setUnidades(j.getUnidades() - unidades)
                                print("Forma de pagamento:")
                                print("1 - Dinheiro")
                                print("2 - Cartão de crédito")
                                opcao = int(input("Digite a opção desejada:"))
                                while opcao < 1 or opcao > 2:
                                    print("Opção inválida!")
                                    opcao = int(input("Digite a opção desejada:"))
                                if opcao == 1:
                                    forma_pagamento = "Dinheiro"                                   
                                elif opcao == 2:
                                    forma_pagamento = "Cartão de crédito"
                                desconto = int(input("Digite o desconto: "))
                                preco = u.getPreco()
                                total = preco * unidades - ((preco * unidades) * (desconto / 100))
                                for j in listaClientes:
                                    if email == j.getEmail() and senha == j.getSenha():
                                        historico_compras = j.getHistoricoCompras()
                                historico_compras.append(Compra(u.getDepartamento(), u.getTipo(), u.getTamanho(), u.getGenero(), unidades, u.getCodigoSerial(), preco, forma_pagamento, desconto, total))
                                for j in listaClientes:
                                    if email == j.getEmail() and senha == j.getSenha():
                                        j.setHistoricoCompras(historico_compras)
                                print("Compra efetuada com sucesso!")
                                print("")
                                break

                elif opcao == 2:
                    consultar_historico_compras(email, senha)
                elif opcao == 3:
                    listarProduto()
                elif opcao == 0:
                    break
                
        else:
            print("Login inválido!")
            print("")


def listar_clientes():
    for i in listaClientes:
        print("Dados do cliente:")
        print("Nome: ", i.getNome())
        print("RG: ", i.getRg())
        print("Endereço: ", i.getEndereco())
        print("Telefone: ", i.getTelefone())
        print("E-mail: ", i.getEmail())
        print("")

def alterarCliente():
    print()
    x = int(input("Digite o RG do cliente: "))
    for i in listaClientes:
        if i.getRg() == x:
            print("1 - Alterar Nome")
            print("2 - Alterar Rg")
            print("3 - Alterar Endereço")
            print("4 - Alterar Telefone")
            print("5 - Alterar Endereço Eletrônico")
            print("6 - Alterar Senha")
            print("0 - Sair")
            print("")
            opcao = int(input("Digite a opção desejada: "))
            while opcao != 0:
                if opcao == 1:
                    nome = input("Digite o novo nome: ")
                    i.setNome(nome)
                elif opcao == 2:
                    rg = int(input("Digite o novo rg: "))
                    i.setRg(rg)
                elif opcao == 3:
                    endereco = input("Digite o novo endereço: ")
                    i.setEndereco(endereco)
                elif opcao == 4:
                    telefone = int(input("Digite o novo telefone: "))
                    i.setTelefone(telefone)
                elif opcao == 5:
                    email = input("Digite o novo endereço eletrônico: ")
                    i.setEmail(email)
                elif opcao == 6:
                    senha = input("Digite a nova senha: ")
                    i.setSenha(senha)
                while opcao < 0 or opcao > 6:
                    print("Opção inválida!")
                opcao = int(input("Digite a opção desejada: "))
            print("")
            break
        else:
            print("Cliente não encontrado!")
            print("")
      
      
def cadastrar_Funcionario():
    print('Opções de cargo: ')
    print('1 - Vendedor')
    print('2 - Administrativo')
    print('3 - Gerente')
    print('4 - Auxiliar de Limpeza')
    cargo = int(input('Digite o cargo desejado: '))
    while cargo < 1 or cargo > 4:
        print('Opção inválida!')
        cargo = int(input('Digite o cargo desejado: '))
    if cargo == 1:
        cargo = 'Vendedor'
    elif cargo == 2:
        cargo = 'Administrativo'
    elif cargo == 3:
        cargo = 'Gerente'
    elif cargo == 4:
        cargo = 'Auxiliar de Limpeza'

    nome = input('Nome: ')
    rg = int(input('RG: '))
    matricula = int(input('Matricula: '))
    telefone = int(input('Telefone: '))
    salario = float(input('Salario: '))
    if cargo == 'Vendedor':
        venda = float(input('Venda: '))
        adicional = float(input('Adicional: '))
        vendedor = Vendedor(nome, rg, matricula, telefone, salario, venda, adicional, cargo)
        listaFuncionarios.append(vendedor)
    elif cargo == 'Gerente':
        gerente = Gerente(nome, rg, matricula, telefone, salario, cargo)
        listaFuncionarios.append(gerente)
    elif cargo == 'Auxiliar de Limpeza':
        print('1 - Diurno')
        print('2 - Noturno')
        turno = ''
        tipo = int(input('Tipo: '))
        while tipo < 1 or tipo > 2:
            print('Opção invalida!')
            tipo = int(input('Tipo: '))
        if tipo == 1:
            turno = 'Diurno'
        elif tipo == 2:
            turno = 'Noturno' 
        auxiliar = AuxLimpeza(nome, rg, matricula, telefone, salario, cargo, turno)
        listaFuncionarios.append(auxiliar)
    elif cargo == 'Administrativo':
        administrativo = Administrativo(nome, rg, matricula, telefone, salario, cargo)
        listaFuncionarios.append(administrativo)
    print('Funcionario cadastrado com sucesso!')
    
def listar_Funcionario():
    for i in listaFuncionarios:
        print('')
        print('/'*50)
        print('Dados do funcionário:')
        print('Nome: ', i.getNome())
        print('RG: ', i.getRg())
        print('Matricula: ', i.getMatricula())
        print('Telefone: ', i.getTelefone())
        print('Salario: ', i.getSalario())
        print('Cargo: ', i.getCargo())
        if i.getCargo() == 'Vendedor':
            print('Venda: ', i.getVenda())
            print('Adicional: ', i.getAdicional())
        if i.getCargo() == 'Auxiliar de Limpeza':
            print('Turno: ', i.getTurno())
        print('/'*50)
        print('')

def alterar_Funcionario():
    print()
    print("Alterar dados do funcionário: ")
    x = int(input("Digite o RG do funcionário: "))
    for i in listaFuncionarios:
        if i.getRg() == x:
            print("1 - Alterar Nome")
            print("2 - Alterar Rg")
            print("3 - Alterar Matricula")
            print("4 - Alterar Telefone")
            print("5 - Alterar Salario")
            print("0 - Sair")
            print("")
            opcao = int(input("Digite a opção desejada:"))
            while opcao !=0:
                if opcao == 1:
                    novoNome = input("Digite o novo nome: ")
                    i.setNome(novoNome)
                elif opcao == 2:
                    novoRg = int(input("Digite o novo RG: "))
                    i.setRg(novoRg)
                elif opcao == 3:
                    novoMatricula = int(input("Digite a nova Matricula: "))
                    i.setMatricula(novoMatricula)
                elif opcao == 4:
                    novoTelefone = int(input("Digite o novo Telefone: "))
                    i.setTelefone(novoTelefone)
                elif opcao == 5:
                    novoSalario = float(input("Digite o novo Salario: "))
                    i.setSalario(novoSalario)
                while opcao < 0 or opcao > 5:
                    print("Opção inválida!")
                opcao = int(input("Digite a opção desejada: "))
                print("")
                break
        else:
            print("Funcionario não encontrado!")
            print("")

def cadastrarProduto():
    print()
    print("Cadastro de Produto\n")
    departamento = input("Digite o departamento (Adulto ou Infantil): ").lower()
    while departamento.lower() not in ["adulto", "infantil", ]:
        print("Departamento inválido. Por favor, digite 'Adulto' ou 'Infantil'.")
        departamento = input("Digite o departamento: ").lower()

    tipo = input("Digite o tipo: ")
    tamanho = input("Digite o tamanho (PP, P, M, G, GG, XG): ").upper()
    while tamanho.upper() not in ["PP", "P", "M", "G", "GG", "XG"]:
        print("Tamanho inválido. Por favor, digite um tamanho válido.")
        tamanho = input("Digite o tamanho: ").upper()

    genero = input("Digite o gênero (Feminino ou Masculino ou Unissex): ")
    while genero.lower() not in ["feminino", "masculino", "unissex"]:
        print("Gênero inválido. Por favor, digite 'Feminino' ou 'Masculino'.")
        genero = input("Digite o gênero: ").lower()

    unidades = int(input("Digite a quantidade de unidades: "))
    while unidades <= 0:
        print("Quantidade inválida. Por favor, digite um número positivo.")
        unidades = int(input("Digite a quantidade de unidades: "))
    
    codigo_serial = input("Digite o código serial: ")
    for i in listaProdutos:
        while i.getCodigoSerial() == codigo_serial:
            print("Código serial já cadastrado. Por favor, digite um código serial válido.")
            codigo_serial = input("Digite o código serial: ")

    preco = float(input("Digite o preço: "))
    while preco <= 0:
        print("Preço inválido. Por favor, digite um número positivo.")
        preco = float(input("Digite o preço: "))

    listaProdutos.append(Produto(departamento, tipo, tamanho.upper(), genero.lower(), unidades, codigo_serial, preco))
    print("Produto cadastrado com sucesso!\n")
    

def listarProduto():
    for w in listaProdutos:
        print("")
        print("/"*50)
        print("Departamento: ", w.getDepartamento())
        print("Tipo produto: ", w.getTipo())
        print("Tamanho: ", w.getTamanho())
        print("Gênero: ", w.getGenero())
        print("Unidades: ", w.getUnidades())
        print("Código serial: ", w.getCodigoSerial())
        print("Preço: ", w.getPreco())
        print("/"*50)
        print("")

def alterarProduto():
    print()
    print("Alterar dados do Produto\n")
    codigo_serial = input("Digite o código serial do produto: ")
    for i in listaProdutos:
        if i.getCodigoSerial() == codigo_serial:
            while True:
                print("1 - Alterar Departamento")
                print("2 - Alterar Tipo")
                print("3 - Alterar Tamanho")
                print("4 - Alterar Gênero")
                print("5 - Alterar Unidades")
                print("6 - Alterar Código serial")
                print("7 - Alterar Preço")
                print("0 - Sair")
                print("")
                opcao = int(input("Digite a opção desejada: "))
                if opcao == 1:
                    novoDepartamento = input("Digite o novo departamento: ").lower()
                    while novoDepartamento not in ["adulto", "infantil"]:
                        print("Departamento inválido. Por favor, digite 'Adulto' ou 'Infantil'.")
                        novoDepartamento = input("Digite o novo departamento: ").lower()
                    i.setDepartamento(novoDepartamento)
                elif opcao == 2:
                    novoTipo = input("Digite o novo tipo: ")
                    i.setTipo(novoTipo)
                elif opcao == 3:
                    novoTamanho = input("Digite o novo tamanho: ").upper()
                    while novoTamanho not in ["PP", "P", "M", "G", "GG", "XG"]:
                        print("Tamanho inválido. Por favor, digite um tamanho válido.")
                        novoTamanho = input("Digite o novo tamanho: ").upper()
                    i.setTamanho(novoTamanho)
                elif opcao == 4:
                    novoGenero = input("Digite o novo gênero: ").lower()
                    while novoGenero not in ["feminino", "masculino", "unissex"]:
                        print("Gênero inválido. Por favor, digite 'Feminino' ou 'Masculino' ou 'Unissex'.")
                        novoGenero = input("Digite o novo gênero: ").lower()
                    i.setGenero(novoGenero)
                elif opcao == 5:
                    novoUnidades = int(input("Digite a nova quantidade de unidades: "))
                    i.setUnidades(novoUnidades)
                elif opcao == 6:
                    novoCodigoSerial = int(input("Digite o novo código serial: "))
                    i.setCodigoSerial(novoCodigoSerial)
                elif opcao == 7:
                    novoPreco = float(input("Digite o novo preço: "))
                    i.setPreco(novoPreco)
                elif opcao == 0:
                    break
                else:
                    print("Opção inválida!")
                    continue
                print("")
        else:
            print("Produto não encontrado!")
            print("")

def removerProduto():
    print()
    print("Remover Produto\n")
    codigo_serial = int(input("Digite o código serial do produto: "))
    for i in listaProdutos:
        if i.getCodigoSerial() == codigo_serial:
            listaProdutos.remove(i)
            print("Produto removido com sucesso!")
            print("")
        else:
            print("Produto não encontrado!")
            print("")

def removerCliente():
    print()
    print("Remover Cliente\n")
    Rg = int(input("Digite o RG do cliente: "))
    for i in listaClientes:
        if i.getRg() == Rg:
            listaClientes.remove(i)
            print("Cliente removido com sucesso!")
            print("")
        else:
            print("Cliente não encontrado!")
            print("")

def remover_Funcionario():
    print()
    print("Remover Funcionário\n")
    matricula = int(input("Digite o número de matrícula do funcionário: "))
    for i in listaFuncionarios:
        if i.getMatricula() == matricula:
            listaFuncionarios.remove(i)
            print("Funcionário removido com sucesso!")
            print("")
        else:
            print("Funcionário não encontrado!")
            print("")


while True:
    opcao = Menu()
    if opcao == 1:
        print("")
        cadastrarCliente()
    elif opcao == 2:
        print("")
        listar_clientes()
    elif opcao == 3:
        print("")
        alterarCliente()
    elif opcao == 4:
        print("")
        cadastrar_Funcionario()
    elif opcao == 5:
        print("")
        listar_Funcionario()
    elif opcao == 6:
        print("")
        alterar_Funcionario()
    elif opcao == 7:
        print("")
        cadastrarProduto()
    elif opcao == 8:
        print("")
        listarProduto()
    elif opcao == 9:
        print("")
        alterarProduto()
    elif opcao == 10:
        print("")
        login_cliente()
    elif opcao == 11:
        print("")
        removerCliente()
    elif opcao == 12:
        print("")
        remover_Funcionario()
    elif opcao == 13:
        print("")
        removerProduto()

    elif opcao == 0:
        break
    else: 
        print("Opção Inválida.")
