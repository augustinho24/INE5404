numeros = [int(x) for x in input().split()]

while not len(numeros) <= 5:
    numeros = [int(x) for x in input("CU: ").split()]

numeros.reverse()
print(*numeros)

