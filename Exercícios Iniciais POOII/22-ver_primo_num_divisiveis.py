import math

n = int(input())
num_divisiveis = []

for u in range (2, n+1):
    if u == 1:
        verifica_primo = False
    elif u != 2 and u % 2 == 0:
        verifica_primo = False
    else:
        verifica_primo = True
        raiz = int(math.sqrt(u))
        for i in range(3, raiz+1, 2):
            if u % i == 0:
                verifica_primo = False

if verifica_primo == True:
    print("É primo")
else:
    for i in range(1, n+1):
        if n % i == 0:
            num_divisiveis.append(i)
    print("Não é primo, é divisível por: ",*num_divisiveis)