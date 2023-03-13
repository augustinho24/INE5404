import math

n = int(input())
for u in range (0,n+1):
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
print(verifica_primo)
              
