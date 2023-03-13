qtd_par = 0
qtd_impar = 0

numeros = [int(x) for x in input().split()]
while len(numeros) < 10:
    numeros = [int(x) for x in input("Inválido: ").split()]

for i in range(10):
    if numeros[i] % 2 == 0 and numeros[i] != 0:
        qtd_par += 1
    else:
        if numeros[i] != 0:
            qtd_impar +=1
print(f"Pares: {qtd_par} Ímpares: {qtd_impar}")
    


