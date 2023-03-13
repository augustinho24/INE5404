def aumento_sal (x,j,k,i):
    return x+(x*(j/100)*(i-k))

salario_inicial = float(input("Digite o salário inicial: "))
aumento = float(input("Digite o aumento percentual: "))
ano_de_inicio = int(input("Digite o ano de início: "))
ano_atual = int(input("Digite o ano de fim: "))

print(f"Salário inicial: {salario_inicial}")
print(f"Salário atual: {aumento_sal(salario_inicial,aumento,ano_de_inicio,ano_atual)}")