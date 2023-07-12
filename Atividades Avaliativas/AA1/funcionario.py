class Funcionario:
    def __init__(self, nome, rg, matricula, telefone, salario, cargo):
        self.nome = nome
        self.rg = rg
        self.matricula = matricula
        self.telefone = telefone
        self.salario = salario
        self.cargo = cargo

    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome

    def getRg(self):
        return self.rg
    def setRg(self, rg):
        self.rg = rg

    def getMatricula(self):
        return self.matricula
    def setMatricula(self, matricula):
        self.matricula = matricula

    def getTelefone(self):
        return self.telefone
    def setTelefone(self, telefone):
        self.telefone = telefone

    def getSalario(self):
        return self.salario
    def setSalario(self, salario):
        self.salario = salario
    
    def getCargo(self):
        return self.cargo
    def setCargo(self, cargo):
        self.cargo = cargo

class Vendedor(Funcionario):
    def __init__(self, nome, rg, matricula, telefone, salario, venda, adicional, cargo):
        super().__init__(nome, rg, matricula, telefone, salario, cargo)
        self.venda = venda
        self.adicional = adicional

    def getVenda(self):
        return self.venda
    def set(self, venda):
        self.venda = venda

    def getAdicional(self):
        return self.adicional
    def setAdicional(self, adicional):
        self.adicional = adicional

class Administrativo(Funcionario):
    def __init__(self, nome, rg, matricula, telefone, salario, cargo):
        super().__init__(nome, rg, matricula, salario, telefone, cargo)
  

def getAdministrativo(self):
    return self.administrativo
def setAdministrativo(self, administrativo):
    self.administrativo = administrativo

class Gerente(Funcionario):
    def __init__(self, nome, rg, matricula, telefone, salario, cargo):
        super().__init__(nome, rg, matricula, salario, telefone, cargo)      

class AuxLimpeza(Funcionario):
    def __init__(self, nome, rg, matricula, telefone, salario, cargo, turno):
        super().__init__(nome, rg, matricula, telefone, salario, cargo)
        self.turno = turno

    def getTurno(self):
        return self.turno
    def setTurno(self, turno):
        self.turno = turno
