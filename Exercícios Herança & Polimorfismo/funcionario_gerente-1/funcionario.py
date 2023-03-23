class Funcionario():
    def __init__(self, num_matricula, cpf, nome, sexo, idade, salario, cargo, turno, adicional):
        self.num_matricula = num_matricula
        self.cpf = cpf
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.salario = salario
        self.cargo = cargo
        self.turno = turno
        self.adicional = adicional
    
class Assistente(Funcionario):
    def __init__(self, num_matricula, cpf, nome, sexo, idade, salario, cargo, turno, adicional):
        super().__init__(num_matricula, cpf, nome, sexo, idade, salario, cargo, turno, adicional)
class Assistente_Tecnico(Funcionario):
    def __init__(self, num_matricula, cpf, nome, sexo, idade, salario, cargo, turno, adicional):
        super().__init__(num_matricula, cpf, nome, sexo, idade, salario, cargo, turno, adicional)

    def get_num_matricula(self):
        return self.num_matricula
    def get_cpf(self):
        return self.cpf
    def get_nome(self):
        return self.nome
    def get_sexo(self):
        return self.sexo
    def get_idade(self):
        return self.idade
    def get_salario(self):
        return self.salario
    def get_cargo(self):
        return self.cargo
    def get_turno(self):
        return self.turno
    def get_adicional(self):
        return self.adicional
    def set_num_matricula(self, num_matricula):
        self.num_matricula = num_matricula
    def set_cpf(self, cpf):
        self.cpf = cpf
    def set_nome(self, nome):
        self.nome = nome
    def set_sexo(self, sexo):
        self.sexo = sexo
    def set_idade(self, idade):
        self.idade = idade
    def set_salario(self, salario):
        self.salario = salario
    def set_cargo(self, cargo):
        self.cargo = cargo
    def set_turno(self, turno):
        self.turno = turno
    def set_adicional(self, adicional):
        self.adicional = adicional
    



    
