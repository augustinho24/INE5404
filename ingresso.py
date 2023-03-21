class Ingresso():
    def __init__(self,nome,valor,tipo):
        self.valor = valor
        self.nome = nome
        self.tipo = tipo

class VIP(Ingresso):
    def __init__(self, nome, valor, tipo, adicional_vip):
        super().__init__(nome, valor, tipo)
        self.valor = valor + adicional_vip
        self.tipo = "VIP"

class Normal(Ingresso):
    def __init__(self, nome, valor, tipo):
        super().__init__(nome, valor, tipo)
        self.tipo = "Normal"

class CamaroteInferior(VIP):
    def __init__(self, nome, valor, tipo, adicional_vip,camarote):
        super().__init__(nome, valor, tipo, adicional_vip, camarote)
        self.camarote = "Camarote Inferior"

class CamaroteSuperior(VIP):
    def __init__(self, nome, valor, tipo, adicional_vip,camarote,adicional_camarote):
        super().__init__(nome, valor, tipo, adicional_vip, camarote, adicional_camarote)
        self.camarote = "Camarote Superior"
        self.valor = valor + adicional_vip + adicional_camarote

def get_nome(self):
    return self.nome

def get_tipo(self):
    return self.tipo

def get_valor (self):
    return self.valor

def get_adicional_vip (self):
    return self.adicional_vip

def get_camarote(self):
    return self.camarote

def get_adicional_camarote(self):
    return self.adicional_camarote
    







    
    






        


        
