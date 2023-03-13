import math

n = int(input())
'''qtd_primos = 0'''
num_primos = [] 

for u in range (1, n+1):
    if u == 1:
        verifica_primo = False
    elif u != 2 and u % 2 == 0:
        verifica_primo = False
    else:
        verifica_primo = True
        num_primos.append(u)
        '''qtd_primos += 1'''
        raiz = int(math.sqrt(u))
        for i in range(3, raiz+1, 2):
            if u % i == 0:
                verifica_primo = False
                '''qtd_primos -= 1'''
                num_primos.pop(num_primos.index(u))
                
imprimir_lista_primos = ','.join([str(num_primos) for num_primos in num_primos])         
                



print(f"Números primos até {n}:", imprimir_lista_primos)