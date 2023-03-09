n1,n2 = [int(x) for x in input().split()]

numeros_entre = []

for i in range(n1+1, n2):
    numeros_entre.append(i)
print(*numeros_entre)