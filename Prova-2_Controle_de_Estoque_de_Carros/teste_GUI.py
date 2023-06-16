from tkinter import Tk, Label, Entry, Button
from carro import Carro
from estoque import Estoque
from controller_estoque import ControllerEstoque

# Criação do estoque
estoque = Estoque()
controller_estoque = ControllerEstoque()
IntVar = 0

# Criação da função de cadastro


def cadastrar_carro():
    id = int(entry_id.get())
    marca = entry_marca.get()
    modelo = entry_modelo.get()
    ano_fabricacao = int(entry_ano_fabricacao.get())
    preco = float(entry_preco.get())
    estado = "Novo" if var_estado.get() == 1 else "Usado"
    
    carro = Carro(id, marca, modelo, ano_fabricacao, preco, estado)
    controller_estoque.estoque.adicionar_carro(carro)
    limpar_campos()
    listar_carros()

def limpar_campos():
    entry_id.delete(0, 'end')
    entry_marca.delete(0, 'end')
    entry_modelo.delete(0, 'end')
    entry_ano_fabricacao.delete(0, 'end')
    entry_preco.delete(0, 'end')
    var_estado.set(1)

def listar_carros():
    # Implemente o código para listar os carros na interface
    pass

# Criação da janela
root = Tk()
root.title("Cadastro de Carros")

# Criação dos rótulos
label_id = Label(root, text="ID:")
label_id.grid(row=0, column=0)

label_marca = Label(root, text="Marca:")
label_marca.grid(row=1, column=0)

label_modelo = Label(root, text="Modelo:")
label_modelo.grid(row=2, column=0)

label_ano_fabricacao = Label(root, text="Ano de Fabricação:")
label_ano_fabricacao.grid(row=3, column=0)

label_preco = Label(root, text="Preço:")
label_preco.grid(row=4, column=0)

# Criação dos campos de entrada
entry_id = Entry(root)
entry_id.grid(row=0, column=1)

entry_marca = Entry(root)
entry_marca.grid(row=1, column=1)

entry_modelo = Entry(root)
entry_modelo.grid(row=2, column=1)

entry_ano_fabricacao = Entry(root)
entry_ano_fabricacao.grid(row=3, column=1)

entry_preco = Entry(root)
entry_preco.grid(row=4, column=1)

# Criação do campo de seleção de estado
var_estado = IntVar()
checkbutton_estado = Checkbutton(root, text="Novo", variable=var_estado)
checkbutton_estado.grid(row=5, column=0, columnspan=2)

# Criação do botão de cadastro
button_cadastrar = Button(root, text="Cadastrar", command=cadastrar_carro)
button_cadastrar.grid(row=6, column=0, columnspan=2)

# Exibição da janela
root.mainloop()