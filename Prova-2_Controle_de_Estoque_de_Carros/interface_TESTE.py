from controller_estoque import ControllerEstoque

import tkinter as tk
from tkinter import messagebox

class EstoqueApp(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("Controle de Estoque")
        self.controller = controller

        # Elementos gráficos
        self.label_marca = tk.Label(self, text="Marca do carro:")
        self.entry_marca = tk.Entry(self)
        self.button_listar_por_marca = tk.Button(self, text="Listar por marca", command=self.listar_por_marca)

        # Posicionamento dos elementos
        self.label_marca.pack()
        self.entry_marca.pack()
        self.button_listar_por_marca.pack()

    def listar_por_marca(self):
        marca = self.entry_marca.get()
        self.controller.listar_carros_por_marca(marca)


# Criação do objeto ControllerEstoque e da interface EstoqueApp
controller = ControllerEstoque()
app = EstoqueApp(controller)
app.mainloop()