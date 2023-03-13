N = int(input("Montar a tabuada de: "))
minimo = int(input("- Começar por: "))
maximo = int(input("- Terminar em: "))

while minimo > maximo:
    print("Inválido, digte novamente:")
    minimo = int(input("- Começar por: "))
    maximo = int(input("- Terminar em: "))

for i in range(minimo,maximo+1): print(f"{N} X {i} = {N*i}")