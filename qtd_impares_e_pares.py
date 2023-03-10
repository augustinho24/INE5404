qtd_par = 0
qtd_impar = 0

numeros = []
for u in range(10):
    num = int(input())
    numeros.append(num)

for i in range(10):
    if numeros[i] % 2 == 0 and numeros[i] != 0:
        qtd_par += 1
    else:
        if numeros[i] != 0:
            qtd_impar +=1 
    

