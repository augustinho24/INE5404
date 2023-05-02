matriz = [[], [], [], [], [], [], [], [], []]

for i in range(len(matriz)):
    matriz[i] = []

while True:
    venda_semanal = float(input())
    if venda_semanal == -1: break
    venda_semanal += 0.09
    verificar_primeiro_digito = int(str(venda_semanal)[0])
    if venda_semanal >= 1000:
        matriz[8].append(venda_semanal)
    else:
        matriz[verificar_primeiro_digito-2].append(venda_semanal)

print()
print("$200 - $299:", len(matriz[0]))
print("$300 - $399:", len(matriz[1]))
print("$400 - $499:", len(matriz[2]))
print("$500 - $599:", len(matriz[3]))
print("$600 - $699:", len(matriz[4]))
print("$700 - $799:", len(matriz[5]))
print("$800 - $899:", len(matriz[6]))
print("$900 - $999:", len(matriz[7]))
print("$1000 em diante:", len(matriz[8]))