from controller_estoque import ControllerEstoque
from estoque import Estoque
from tkinter import *
from tkinter import messagebox, Toplevel
import tkinter as tk


class ViewEstoque:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Controle de Estoque da Loja de Carros")
        self.window.geometry("500x500")
        self.window.resizable(False, False)
        self.controller_estoque = ControllerEstoque()
        self.estoque = Estoque()
        self.menu()
        self.window.mainloop()

    def cadastrar_carro_interface(self):
        try:
            id = int(self.entry_id.get())
            marca = self.entry_marca.get()
            modelo = self.entry_modelo.get()
            ano_fabricacao = int(self.entry_ano_fabricacao.get())
            preco = float(self.entry_preco.get())
            estado = self.entry_estado.get()
            if self.estoque.verifica_id(id):
                messagebox.showerror("Erro", "Erro: id já existente.")
            elif estado != "Novo" and estado != "Usado":
            #if estado != "Novo" and estado != "Usado" or self.estoque.verifica_id(id):
                messagebox.showerror("Erro", "Erro: estado inválido ou ID já existente.")
            else:
                self.controller_estoque.cadastrar_carro(id, marca, modelo, ano_fabricacao, preco, estado)
                messagebox.showinfo("Sucesso", "Carro cadastrado com sucesso.")
        except ValueError:
            messagebox.showerror("Erro", "Erro: id inválido.")

    def atualizar_carro_interface(self):
        try:
            id = int(self.entry_id.get())
            marca = self.entry_marca.get()
            modelo = self.entry_modelo.get()
            ano_fabricacao = int(self.entry_ano_fabricacao.get())
            preco = float(self.entry_preco.get())
            estado = self.entry_estado.get().capitalize()
            while estado != "Novo" and estado != "Usado":
                messagebox.showerror("Erro", "Erro: estado inválido.")
            self.controller_estoque.atualizar_carro(id, marca, modelo, ano_fabricacao, preco, estado)
            messagebox.showinfo("Sucesso", "Carro atualizado com sucesso.")
        except ValueError:
            messagebox.showerror("Erro", "Erro: id inválido.")

    def remover_carro_interface(self):
        try:
            id = int(self.entry_id.get())
            self.controller_estoque.remover_carro(id)
            messagebox.showinfo("Sucesso", "Carro removido com sucesso.")
            if self.estoque.verifica_id(id):
                messagebox.showerror("Erro", "Erro: id não encontrado.")
        except ValueError:
            messagebox.showerror("Erro", "Erro: id inválido.")

    def listar_carros_interface(self):
        carros = self.controller_estoque.listar_carros()

        # Criação da nova janela
        janela_listagem = Toplevel(self.window)
        janela_listagem.title("Lista de Carros")
        janela_listagem.geometry("800x600")

        # Criação da listbox
        listbox_listar_carros = Listbox(janela_listagem, width=100, height=40)

        if not carros:
            listbox_listar_carros.insert(END, "Nenhum carro cadastrado.")
        else:
            for carro in carros:
                
                id = carro.id
                marca = carro.marca
                modelo = carro.modelo
                ano_fabricacao = carro.ano_fabricacao
                preco = carro.preco
                estado = carro.estado

             
                car_info = f"ID: {id}, Marca: {marca}, Modelo: {modelo}, Ano de Fabricação: {ano_fabricacao}, Preço: {preco}, Estado: {estado}"

                listbox_listar_carros.insert(END, car_info)

        listbox_listar_carros.pack(padx=30, pady=30)

        # Definição da janela como modal (bloqueia a interação com a janela principal enquanto estiver aberta)
        janela_listagem.transient(self.window)
        janela_listagem.grab_set()
        self.window.wait_window(janela_listagem)

    def listar_carros_por_marca_interface(self):
        marca = self.entry_listar_carros_por_marca.get()
        carros = self.controller_estoque.listar_carros_por_marca(marca)
    
        # Criação da nova janela
        janela_listagem = Toplevel(self.window)
        janela_listagem.title(f"Lista de Carros da Marca {marca}")
        janela_listagem.geometry("800x600")
    
        # Criação da listbox
        listbox_listar_carros_por_marca = Listbox(janela_listagem, width=100, height=40)
    
        if not carros:
            listbox_listar_carros_por_marca.insert(END, f"Nenhum carro da marca {marca} encontrado.")
        else:
            for carro in carros:
                id = carro.id
                marca = carro.marca
                modelo = carro.modelo
                ano_fabricacao = carro.ano_fabricacao
                preco = carro.preco
                estado = carro.estado
    
                car_info = f"ID: {id}, Marca: {marca}, Modelo: {modelo}, Ano de Fabricação: {ano_fabricacao}, Preço: R$ {preco}, Estado: {estado}"
    
                listbox_listar_carros_por_marca.insert(END, car_info)
    
        listbox_listar_carros_por_marca.pack(padx=30, pady=30)

    def calcular_media_precos_interface(self):
        media_precos = self.controller_estoque.calcular_media_precos()
        messagebox.showinfo("Média dos preços", f"Média dos preços dos carros: R$ {media_precos:.2f}")

    def menu(self):
        # Criação dos widgets
        label_id = Label(self.window, text="ID:")
        label_id.grid(row=0, column=0, padx=10, pady=10)
        self.entry_id = Entry(self.window)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)

        label_marca = Label(self.window, text="Marca:")
        label_marca.grid(row=1, column=0, padx=10, pady=10)
        self.entry_marca = Entry(self.window)
        self.entry_marca.grid(row=1, column=1, padx=10, pady=10)

        label_modelo = Label(self.window, text="Modelo:")
        label_modelo.grid(row=2, column=0, padx=10, pady=10)
        self.entry_modelo = Entry(self.window)
        self.entry_modelo.grid(row=2, column=1, padx=10, pady=10)

        label_ano_fabricacao = Label(self.window, text="Ano de Fabricação:")
        label_ano_fabricacao.grid(row=3, column=0, padx=10, pady=10)
        self.entry_ano_fabricacao = Entry(self.window)
        self.entry_ano_fabricacao.grid(row=3, column=1, padx=10, pady=10)

        label_preco = Label(self.window, text="Preço:")
        label_preco.grid(row=4, column=0, padx=10, pady=10)
        self.entry_preco = Entry(self.window)
        self.entry_preco.grid(row=4, column=1, padx=10, pady=10)

        label_estado = Label(self.window, text="Estado:")
        label_estado.grid(row=5, column=0, padx=10, pady=10)
        self.entry_estado = Entry(self.window)

        self.entry_estado.grid(row=5, column=1, padx=10, pady=10)

        button_cadastrar = Button(self.window, text="Cadastrar", command=self.cadastrar_carro_interface)
        button_cadastrar.grid(row=6, column=0, padx=10, pady=10)

        button_atualizar = Button(self.window, text="Atualizar", command=self.atualizar_carro_interface)
        button_atualizar.grid(row=6, column=1, padx=10, pady=10)

        button_remover = Button(self.window, text="Remover", command=self.remover_carro_interface)
        button_remover.grid(row=7, column=0, padx=10, pady=10)

        button_listar_carros = Button(self.window, text="Listar Carros", command=self.listar_carros_interface)
        button_listar_carros.grid(row=7, column=1, padx=10, pady=10)


        label_listar_carros_por_marca = Label(self.window, text="Marca:")
        label_listar_carros_por_marca.grid(row=10, column=0, padx=10, pady=10)
        self.entry_listar_carros_por_marca = Entry(self.window)
        self.entry_listar_carros_por_marca.grid(row=10, column=1, padx=10, pady=10)
        button_calcular_media_precos = Button(self.window, text="Calcular Média dos Preços", command=self.calcular_media_precos_interface)
        button_calcular_media_precos.grid(row=12, column=0, padx=10, pady=10)

        button_listar_carros_por_marca = Button(self.window, text="Listar Carros por Marca",
                                                command=self.listar_carros_por_marca_interface)
        button_listar_carros_por_marca.grid(row=12, column=1, padx=10, pady=10)

        #self.listbox_listar_carros_por_marca = Listbox(self.window, width=40, height=10)
       

        
        self.window.grid_rowconfigure(14, weight=1)
        self.window.mainloop()

