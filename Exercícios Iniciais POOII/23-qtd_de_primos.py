import math


n = int(input())
qtd_primos = 0
qtd_divisoes = 0 

for u in range (1, n+1):
    if u == 1:
        verifica_primo = False
    elif u != 2 and u % 2 == 0:
        verifica_primo = False
    else:
        verifica_primo = True
        qtd_divisoes = 1
        if u != 2:
            qtd_primos += 1
            raiz = int(math.sqrt(u))
            divisoes = 0
            for i in range(3, raiz+1, 2):
                divisoes = 0
                if u % i == 0:
                    verifica_primo = False
                    qtd_primos -= 1
                    break
            qtd_divisoes += divisoes



print(f"Quantidade de números primos: {qtd_primos}")
print(f"Quantidade de divisões: {qtd_divisoes}")